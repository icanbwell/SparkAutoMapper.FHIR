from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirValueSet,
)


def test_generator_get_value_sets() -> None:
    print("")
    value_sets: List[FhirValueSet] = FhirXmlSchemaParser.get_value_sets()
    print(value_sets)
