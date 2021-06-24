from pathlib import Path
from typing import List

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import (
    FhirXmlSchemaParser,
    FhirValueSet,
)


def test_generator_get_v2_code_systems() -> None:
    print("")
    data_dir: Path = Path(__file__).parent.joinpath("./")
    value_sets: List[FhirValueSet] = FhirXmlSchemaParser.get_v2_code_systems(
        data_dir=data_dir
    )
    print(value_sets)
