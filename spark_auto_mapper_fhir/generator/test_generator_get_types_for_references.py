from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirReferenceType,
)


def test_generator_get_types_for_references() -> None:
    print("")
    references: List[FhirReferenceType] = FhirXmlSchemaParser.get_types_for_references()
    print(references)
