from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
# noinspection PyUnresolvedReferences
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.plan_definition import PlanDefinition
from spark_auto_mapper_fhir.valuesets.publication_status import PublicationStatusCode


def test_auto_mapper_fhir_plan_definition(spark_session: SparkSession) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01', "female"),
            (2, 'Vidal', 'Michael', '1970-02-02', None),
        ],
        ['member_id', 'last_name', 'first_name', 'date_of_birth', "my_gender"]
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).complex(
        PlanDefinition(
            id_=FhirId(A.column("member_id")),
            status=PublicationStatusCode.Active
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(
        source_df=source_df
    )
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    result_df.printSchema()
    result_df.show()
