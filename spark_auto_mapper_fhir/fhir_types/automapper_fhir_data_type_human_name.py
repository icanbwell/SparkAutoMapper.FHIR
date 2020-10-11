from spark_auto_mapper.automapper_defined_types import AutomapperTextType
from spark_auto_mapper.automapper_value_parser import AutoMapperValueParser
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhirDataTypeHumanName(AutoMapperFhirDataTypeComplexBase):
    def __init__(self, use: AutomapperTextType, family: AutomapperTextType) -> None:
        super().__init__()
        self.value = dict(
            use=AutoMapperValueParser.parse_value(use),
            family=AutoMapperValueParser.parse_value(family),
        )
