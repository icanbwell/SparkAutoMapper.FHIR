from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
# noinspection PyUnresolvedReferences
from pyspark.sql.functions import col, expr, regexp_replace, substring
from pyspark.sql.functions import lit, struct, array, coalesce, to_date
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A
from spark_auto_mapper.helpers.spark_higher_order_functions import filter

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.valuesets.identifier_type import IdentifierTypeCode
from spark_auto_mapper_fhir.valuesets.identifier_use import IdentifierUseCode
from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.valuesets.marital_status import MaritalStatusCode
from spark_auto_mapper_fhir.valuesets.name_use import NameUseCode


def test_auto_mapper_fhir_patient(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01', "F"),
            (2, 'Vidal', 'Michael', '1970-02-02', "M"),
        ],
        ['member_id', 'last_name', 'first_name', 'date_of_birth', "my_gender"]
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).columns(
        patient=Patient(
            id_=FhirId(A.column("member_id")),
            identifier=FhirList(
                [
                    Identifier(
                        use=IdentifierUseCode.Usual,
                        value=A.column("member_id"),
                        type_=CodeableConcept(
                            coding=FhirList(
                                [
                                    Coding(
                                        code=IdentifierTypeCode.
                                        MedicalRecordNumber
                                    )
                                ]
                            )
                        )
                    )
                ]
            ),
            name=FhirList(
                [
                    HumanName(
                        use=NameUseCode("usual"),
                        family=A.column("last_name"),
                        given=FhirList(["first_name", "middle_name"])
                    )
                ]
            ),
            birthDate=A.date(A.column("date_of_birth")),
            maritalStatus=CodeableConcept(
                coding=FhirList(
                    [
                        Coding(
                            code=MaritalStatusCode.Married,
                            system=MaritalStatusCode.codeset
                        )
                    ]
                )
            ),
            gender=AdministrativeGenderCode(
                A.expression(
                    """
    CASE
        WHEN `my_gender` = 'F' THEN 'female'
        WHEN `my_gender` = 'M' THEN 'male'
        ELSE 'other'
    END
    """
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
            lit("Patient").alias("resourceType"),
            substring(
                regexp_replace(col("b.member_id"), r"[^A-Za-z0-9\-\.]", "_"),
                0, 63
            ).alias("id"),
            filter(
                array(
                    struct(
                        lit("usual").alias("use"),
                        struct(
                            filter(
                                array(struct(lit("MR").alias("code"))),
                                lambda x: x.isNotNull()
                            ).alias("coding")
                        ).alias("type"),
                        col("b.member_id").alias("value"),
                    )
                ), lambda x: x.isNotNull()
            ).alias("identifier"),
            filter(
                array(
                    struct(
                        lit("usual").alias("use"),
                        col("b.last_name").alias("family"),
                        filter(
                            array(lit("first_name"), lit("middle_name")),
                            lambda x: x.isNotNull()
                        ).alias("given")
                    )
                ), lambda x: x.isNotNull()
            ).alias("name"),
            expr(
                """CASE WHEN (`my_gender` = F) THEN 'female' WHEN (`my_gender` = M) THEN 'male' ELSE other END"""
            ).alias("gender"),
            coalesce(
                to_date(col("b.date_of_birth"), 'yyyy-MM-dd'),
                to_date(col("b.date_of_birth"), 'yyyyMMdd'),
                to_date(col("b.date_of_birth"), 'MM/dd/yyyy'),
                to_date(col("b.date_of_birth"), 'MM/dd/yy')
            ).alias("birthDate"),
            struct(
                filter(
                    array(
                        struct(
                            lit(
                                "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                            ).alias("system"),
                            lit("M").alias("code"),
                        )
                    ), lambda x: x.isNotNull()
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
