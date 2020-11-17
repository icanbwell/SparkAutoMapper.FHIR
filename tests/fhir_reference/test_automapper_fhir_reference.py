from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
# noinspection PyUnresolvedReferences
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.patient import Patient


def test_auto_mapper_fhir_reference(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi'),
            (2, 'Vidal'),
        ], ['member_id', 'last_name']
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
                reference=FhirReference("Organization", A.column("last_name"))
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
    result_df.printSchema()
    result_df.show(truncate=False)

    assert result_df.where("member_id == 1").selectExpr(
        "patient.managingOrganization.reference"
    ).collect()[0][0] == "Organization/Qureshi"
    assert result_df.where("member_id == 2").selectExpr(
        "patient.managingOrganization.reference"
    ).collect()[0][0] == "Organization/Vidal"
