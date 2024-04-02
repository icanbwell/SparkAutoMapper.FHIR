from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame

# noinspection PyUnresolvedReferences
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.extensions.custom.insurance_plan import (
    InsurancePlanExtension,
)
from spark_auto_mapper_fhir.extensions.custom.insurance_plan_item import (
    InsurancePlanItemExtension,
)


def test_auto_mapper_fhir_reference_short(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, "Qureshi"),
            (2, "Vidal"),
            (3, "Duke"),
        ],
        ["member_id", "last_name"],
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).columns(
        patient=Patient(
            id_=FhirId(A.column("last_name")),
            managingOrganization=Reference(
                reference=FhirReference(
                    "Organization",
                    A.if_regex(
                        A.column("member_id"),
                        "[1-2]",
                        A.column("last_name"),
                        A.concat(A.column("last_name"), "|test"),
                    ),
                )
            ),
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(source_df=source_df)
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    result_df.printSchema()
    result_df.show(truncate=False)

    assert (
        result_df.where("member_id == 1")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/Qureshi"
    )
    assert (
        result_df.where("member_id == 2")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/Vidal"
    )

    assert (
        result_df.where("member_id == 3")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/Duke|test"
    )


def test_auto_mapper_fhir_reference_long(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, "Qureshi"),
            (2, "Vidal"),
            (
                3,
                "1F238EABDF31F1FFEDE1D316B5887.922A7B6A6EB4D9C82C9E7FFC748E8-7C28346B3999CB6F",
            ),
        ],
        ["member_id", "last_name"],
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).columns(
        patient=Patient(
            id_=FhirId(A.column("last_name")),
            managingOrganization=Reference(
                reference=FhirReference(
                    "Organization",
                    A.if_regex(
                        A.column("member_id"),
                        "[1-2]",
                        A.column("last_name"),
                        A.concat(A.column("last_name"), "|test"),
                    ),
                    use_long_id=True,
                )
            ),
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(source_df=source_df)
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    result_df.printSchema()
    result_df.show(truncate=False)

    assert (
        result_df.where("member_id == 1")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/Qureshi"
    )
    assert (
        result_df.where("member_id == 2")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/Vidal"
    )

    assert (
        result_df.where("member_id == 3")
        .selectExpr("patient.managingOrganization.reference")
        .collect()[0][0]
        == "Organization/1F238EABDF31F1FFEDE1D316B5887.922A7B6A6EB4D9C82C9E7FFC748E8-7C28346B3999CB6F|test"
    )


def test_auto_mapper_fhir_reference_reference_pattern(
    spark_session: SparkSession,
) -> None:
    """
    Test reference_pattern is used when pattern for a reference is passed.
    """
    # Arrange
    spark_session.createDataFrame(
        [
            ("AETNA", "First Best Plan |  For Member"),
            ("UHC", "Second Best Plan   For Member"),
        ],
        ["insurance_name", "insurance_plan"],
    ).createOrReplaceTempView("insurance")

    source_df: DataFrame = spark_session.table("insurance")
    source_df.createOrReplaceTempView("insurance_plan")

    # Act
    mapper = AutoMapper(
        view="insurance_plan", source_view="insurance", keys=["insurance_name"]
    ).complex(
        PractitionerRole(
            id_=FhirId(
                A.concat(A.column("insurance_name"), "-", A.column("insurance_plan"))
            ),
            extension=FhirList(
                [
                    InsurancePlanExtension(
                        url=InsurancePlanExtension.codeset,
                        extension=FhirList(
                            [
                                InsurancePlanItemExtension(
                                    url=InsurancePlanItemExtension.codeset,
                                    valueReference=Reference(
                                        reference=FhirReference(
                                            "InsurancePlan",
                                            A.column("insurance_plan"),
                                            reference_pattern=r"[^A-Za-z0-9\-\.]",
                                        )
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            ),
        )
    )

    # Assert
    assert isinstance(mapper, AutoMapper)
    result_df: DataFrame = mapper.transform(df=source_df)

    assert (
        result_df.where(result_df["id"] == "AETNA-First-Best-Plan----For-Member")
        .selectExpr("extension[0].extension[0].valueReference.reference")
        .collect()[0][0]
        == "InsurancePlan/First-Best-Plan----For-Member"
    )
    assert (
        result_df.where(result_df["id"] == "UHC-Second-Best-Plan---For-Member")
        .selectExpr("extension[0].extension[0].valueReference.reference")
        .collect()[0][0]
        == "InsurancePlan/Second-Best-Plan---For-Member"
    )
