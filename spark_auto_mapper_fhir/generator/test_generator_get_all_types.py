from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirEntity,
)


def test_generator_get_all_types() -> None:
    print("")
    entities: List[FhirEntity] = FhirXmlSchemaParser.get_all_property_types()
    print(entities)
