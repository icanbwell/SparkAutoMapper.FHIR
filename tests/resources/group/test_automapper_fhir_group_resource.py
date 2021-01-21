from typing import Dict

from pyspark.sql import SparkSession, DataFrame, Column
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.backbone_elements.group_member_backbone_element import GroupMemberBackboneElement
from spark_auto_mapper_fhir.valuesets.group_type import GroupTypeCode
from spark_auto_mapper_fhir.valuesets.identifier_type import IdentifierTypeCode

from spark_auto_mapper_fhir.complex_types.coding import Coding

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.complex_types.identifier import Identifier

from spark_auto_mapper_fhir.complex_types.meta import Meta

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A


def test_auto_mapper_fhir_group_resource(spark_session: SparkSession) -> None:
    spark_session.createDataFrame(
        [(1, "practitioner", "affiliated practitioner", 2)],
        ['practitioner_id', 'type', 'name', 'affiliated_id']
    ).createOrReplaceTempView("groups")

    source_df: DataFrame = spark_session.table("groups")

    df = source_df.select("practitioner_id")
    df.createOrReplaceTempView("practioners")

    mapper = AutoMapper(
        view="practioners", source_view="groups", keys=["practitioner_id"]
    ).complex(
        Group(
            id_=FhirId(A.column("practitioner_id")),
            meta=Meta(source="http://medstarhealth.org/provider"),
            identifier=FhirList(
                [
                    Identifier(
                        value=A.column("practitioner_id"),
                        type_=CodeableConcept(
                            coding=FhirList(
                                [
                                    Coding(
                                        system=IdentifierTypeCode.codeset,
                                        code=IdentifierTypeCode(
                                            A.text("PractitionerAffiliation")
                                        ),
                                    )
                                ]
                            )
                        ),
                        system="http://medstarhealth.org",
                    )
                ]
            ),
            type_=GroupTypeCode.practitioner,
            name=A.text("Medstar Affiliated Practitioner"),
            member=FhirList(
                [
                    GroupMemberBackboneElement(
                        entity=Reference(
                            reference=FhirReference(
                                "Practitioner",
                                A.column("affiliated_id"),
                            )
                        ),
                        inactive=False,
                    ),
                ]
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

    result_df.printSchema()
    result_df.show(truncate=False)
