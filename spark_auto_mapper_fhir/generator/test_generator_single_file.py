from pathlib import Path
from pprint import pprint

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import FhirXmlSchemaParser


def test_generator_single_file() -> None:
    print("")
    data_dir: Path = Path(__file__).parent.joinpath("./")
    resource: str = "account.xsd"
    resource_xsd_file: Path = data_dir.joinpath("xsd").joinpath(resource)
    fhir_entities = FhirXmlSchemaParser._generate_classes_for_resource(
        resource_xsd_file
    )

    # now print the result
    for fhir_entity in fhir_entities:
        pprint(fhir_entity)
