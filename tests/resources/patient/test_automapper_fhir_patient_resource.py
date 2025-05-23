from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame

# noinspection PyUnresolvedReferences
from pyspark.sql.functions import col, regexp_replace, substring
from pyspark.sql.functions import coalesce, lit, to_date
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.value_sets.administrative_gender import (
    AdministrativeGenderCode,
)
from spark_auto_mapper_fhir.value_sets.name_use import NameUseCode


def test_auto_mapper_fhir_patient_resource(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, "Qureshi", "Imran", "1970-01-01", "female"),
            (2, "Vidal", "Michael", "1970-02-02", None),
        ],
        ["member_id", "last_name", "first_name", "date_of_birth", "my_gender"],
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).complex(
        Patient(
            id_=FhirId(A.column("member_id")),
            birthDate=A.date(A.column("date_of_birth")),
            name=FhirList(
                [HumanName(use=NameUseCode("usual"), family=A.column("last_name"))]
            ),
            gender=A.if_not_null(
                A.column("my_gender"), AdministrativeGenderCode(A.column("my_gender"))
            ),
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(source_df=source_df)
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    assert len(sql_expressions) == 5
    assert str(sql_expressions["id"]) == str(
        substring(regexp_replace(col("b.member_id"), r"[^A-Za-z0-9\-\.]", "-"), 0, 63)
        .cast("string")
        .alias("id")
    )
    assert str(sql_expressions["resourceType"]) == str(
        lit("Patient").cast("string").alias("resourceType")
    )
    assert str(sql_expressions["birthDate"]) == str(
        coalesce(
            to_date(col("b.date_of_birth"), "y-M-d"),
            to_date(col("b.date_of_birth"), "yyyyMMdd"),
            to_date(col("b.date_of_birth"), "M/d/y"),
        )
        .cast("date")
        .alias("birthDate")
    )
    # assert str(sql_expressions["name"]) == str(
    #     filter(
    #         array(
    #             struct(
    #                 lit("usual").alias("use"),
    #                 col("b.last_name").alias("family"),
    #             )
    #         ), lambda x: x.isNotNull()
    #     ).alias("name")
    # )
    # assert str(sql_expressions["gender"]) == str(
    #     when(col("b.my_gender").isNull(),
    #          None).otherwise(col("b.my_gender")).alias("gender")
    # )

    result_df.printSchema()
    result_df.show()

    assert (
        result_df.where("member_id == 1").selectExpr("name[0].use").collect()[0][0]
        == "usual"
    )
    assert (
        result_df.where("member_id == 1").selectExpr("name[0].family").collect()[0][0]
        == "Qureshi"
    )

    assert (
        result_df.where("member_id == 2").selectExpr("name[0].use").collect()[0][0]
        == "usual"
    )
    assert (
        result_df.where("member_id == 2").selectExpr("name[0].family").collect()[0][0]
        == "Vidal"
    )
