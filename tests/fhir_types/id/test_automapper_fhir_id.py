from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame

# noinspection PyUnresolvedReferences
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.patient import Patient


def test_auto_mapper_fhir_id_short(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, "Qureshi- / &&"),
            (2, " Vidal. "),
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

    # Sample 1
    mapper = AutoMapper(
        view="members_short", source_view="patients", keys=["member_id"]
    ).columns(patient=Patient(id_=FhirId(A.column("last_name"), False, False)))

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(source_df=source_df)
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    result_df.printSchema()
    result_df.show(truncate=False)

    assert (
        result_df.where("member_id == 1").selectExpr("patient.id").collect()[0][0]
        == "Qureshi------"
    )
    assert (
        result_df.where("member_id == 2").selectExpr("patient.id").collect()[0][0]
        == "-Vidal.-"
    )

    assert (
        result_df.where("member_id == 3").selectExpr("patient.id").collect()[0][0]
        == "1F238EABDF31F1FFEDE1D316B5887.922A7B6A6EB4D9C82C9E7FFC748E8-7C2"
    )


def test_auto_mapper_fhir_id_long(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, "Qureshi- / &&"),
            (2, " Vidal. "),
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

    # Sample 1
    mapper = AutoMapper(
        view="members_short", source_view="patients", keys=["member_id"]
    ).columns(patient=Patient(id_=FhirId(A.column("last_name"), use_long_id=True)))

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(source_df=source_df)
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    result_df.printSchema()
    result_df.show(truncate=False)

    assert (
        result_df.where("member_id == 1").selectExpr("patient.id").collect()[0][0]
        == "Qureshi------"
    )
    assert (
        result_df.where("member_id == 2").selectExpr("patient.id").collect()[0][0]
        == "-Vidal.-"
    )

    assert (
        result_df.where("member_id == 3").selectExpr("patient.id").collect()[0][0]
        == "1F238EABDF31F1FFEDE1D316B5887.922A7B6A6EB4D9C82C9E7FFC748E8-7C28346B3999CB6F"
    )
