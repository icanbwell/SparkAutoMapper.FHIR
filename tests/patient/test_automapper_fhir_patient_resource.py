from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
from pyspark.sql.functions import lit, struct, array, coalesce, to_date
# noinspection PyUnresolvedReferences
from pyspark.sql.functions import col
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.automapper_fhir import AutoMapperFhir
from spark_auto_mapper_fhir.automapper_fhir_helpers import AutoMapperFhirHelpers as F


def test_auto_mapper_fhir_patient_resource(spark_session: SparkSession):
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01'),
            (2, 'Vidal', 'Michael', '1970-02-02'),
        ],
        ['member_id', 'last_name', 'first_name', 'date_of_birth']
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapperFhir(
        view="members",
        source_view="patients",
        keys=["member_id"]
    ).withResource(
        resource=F.patient(
            id_=A.column("a.member_id"),
            birthDate=A.date(
                A.column("date_of_birth")
            ),
            name=A.list(
                F.human_name(
                    use="usual",
                    family=A.column("last_name")
                )
            ),
            gender="female"
        )
    )

    sql_expressions: Dict[str, Column] = mapper.get_column_specs()
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    assert len(sql_expressions) == 4
    assert str(sql_expressions["id"]) == str(col("a.member_id").alias("id"))
    assert str(sql_expressions["birthDate"]) == str(
        coalesce(
            to_date(col("date_of_birth"), 'yyyy-MM-dd'),
            to_date(col("date_of_birth"), 'yyyyMMdd'),
            to_date(col("date_of_birth"), 'MM/dd/yy')
        ).alias("birthDate")
    )
    assert str(sql_expressions["name"]) == str(
        array(
            struct(
                lit("usual").alias("use"),
                col("last_name").alias("family"),
            )
        ).alias("name")
    )
    assert str(sql_expressions["gender"]) == str(lit("female").alias("gender"))

    result_df.printSchema()
    result_df.show()

    assert result_df.where("member_id == 1").selectExpr("name[0].use").collect()[0][0] == "usual"
    assert result_df.where("member_id == 1").selectExpr("name[0].family").collect()[0][0] == "Qureshi"

    assert result_df.where("member_id == 2").selectExpr("name[0].use").collect()[0][0] == "usual"
    assert result_df.where("member_id == 2").selectExpr("name[0].family").collect()[0][0] == "Vidal"
