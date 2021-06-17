from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirCodeableType,
)


def test_generator_get_types_for_codeable_concepts() -> None:
    print("")
    codeable_types: List[
        FhirCodeableType
    ] = FhirXmlSchemaParser.get_types_for_codeable_concepts()
    print(codeable_types)
