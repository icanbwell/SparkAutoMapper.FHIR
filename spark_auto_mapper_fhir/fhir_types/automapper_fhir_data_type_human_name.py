from spark_auto_mapper.data_types.automapper_defined_types import AutoMapperTextType
from spark_auto_mapper.helpers.automapper_value_parser import AutoMapperValueParser
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhirDataTypeHumanName(AutoMapperFhirDataTypeComplexBase):
    def __init__(self, use: AutoMapperTextType, family: AutoMapperTextType) -> None:
        super().__init__()
        self.value = dict(
            use=AutoMapperValueParser.parse_value(use),
            family=AutoMapperValueParser.parse_value(family),
        )
