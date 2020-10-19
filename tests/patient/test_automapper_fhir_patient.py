from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
# noinspection PyUnresolvedReferences
from pyspark.sql.functions import col
from pyspark.sql.functions import lit, struct, array, coalesce, to_date
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.automapper_fhir_helpers import AutoMapperFhirHelpers as F

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.valuesets.identifier_type import FhirIdentifierTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.identifier_use import FhirIdentifierUseCode
from spark_auto_mapper_fhir.fhir_types.coding import FhirCoding
from spark_auto_mapper_fhir.fhir_types.valuesets.name_use import FhirNameUseCode


def test_auto_mapper_fhir_patient(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01'),
            (2, 'Vidal', 'Michael', '1970-02-02'),
        ], ['member_id', 'last_name', 'first_name', 'date_of_birth']
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).columns(
        patient=F.patient.map(
            id_=A.column("a.member_id"),
            identifier=FhirList(
                F.identifier.map(
                    use=FhirIdentifierUseCode.Usual,
                    value=A.column("a.member_id"),
                    type_=FhirCodeableConcept.map(
                        coding=FhirCoding.map(
                            code=FhirIdentifierTypeCode.map("MR")
                        )
                    )
                )
            ),
            name=FhirList(
                F.human_name.map(
                    use=FhirNameUseCode.map("usual"),
                    family=A.column("last_name"),
                    given=FhirList(["first_name", "middle_name"])
                )
            ),
            gender=F.codes.administrative_gender.female,
            birthDate=A.date(A.column("date_of_birth")),
            maritalStatus=FhirCodeableConcept.map(
                coding=FhirCoding.map(
                    code=F.codes.marital_status.Married,
                    system=F.codes.marital_status.codeset
                )
            )
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(
        source_df=source_df
    )
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    assert str(sql_expressions["patient"]) == str(
        struct(
            col("a.member_id").alias("id"),
            array(
                struct(
                    lit("usual").alias("use"),
                    struct(struct(lit("MR").alias("code")).alias("coding")
                           ).alias("type"),
                    col("a.member_id").alias("value"),
                )
            ).alias("identifier"),
            array(
                struct(
                    lit("usual").alias("use"),
                    col("last_name").alias("family"),
                    array(lit("first_name"),
                          lit("middle_name")).alias("given")
                )
            ).alias("name"),
            lit("female").alias("gender"),
            coalesce(
                to_date(col("date_of_birth"), 'yyyy-MM-dd'),
                to_date(col("date_of_birth"), 'yyyyMMdd'),
                to_date(col("date_of_birth"), 'MM/dd/yy')
            ).alias("birthDate"),
            struct(
                struct(
                    lit(
                        "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                    ).alias("system"),
                    lit("M").alias("code"),
                ).alias("coding")
            ).alias("maritalStatus")
        ).alias("patient")
    )

    result_df.printSchema()
    result_df.show()

    result_df.where("member_id == 1").select("patient").show()
    result_df.where("member_id == 1").select("patient").printSchema()

    assert result_df.where("member_id == 1").selectExpr(
        "patient.name[0].use"
    ).collect()[0][0] == "usual"
    assert result_df.where("member_id == 1").selectExpr(
        "patient.name[0].family"
    ).collect()[0][0] == "Qureshi"

    # foo = FhirAdministrativeGender.male
    #
    # print(foo)
