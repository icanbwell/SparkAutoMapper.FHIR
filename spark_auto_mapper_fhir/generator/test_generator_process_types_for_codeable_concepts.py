from pathlib import Path
from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirValueSet,
)


def test_generator_process_types_for_codeable_concepts() -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")
    resource: str = "claim.xsd"
    resource_xsd_file: Path = (
        data_dir.joinpath("xsd")
        .joinpath("definitions.xml")
        .joinpath("fhir-all-xsd")
        .joinpath(resource)
    )
    fhir_entities = FhirXmlSchemaParser._generate_classes_for_resource(
        resource_xsd_file
    )

    print("")
    value_sets: List[FhirValueSet] = FhirXmlSchemaParser.get_value_sets()
    print(value_sets)
    FhirXmlSchemaParser.process_types_for_codeable_concepts(
        fhir_entities=fhir_entities, value_sets=value_sets
    )
