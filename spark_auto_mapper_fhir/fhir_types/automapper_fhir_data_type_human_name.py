from typing import Optional

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType
from spark_auto_mapper.helpers.value_parser import AutoMapperValueParser
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhirDataTypeHumanName(AutoMapperFhirDataTypeComplexBase):
    def __init__(self,
                 use: Optional[AutoMapperTextInputType],
                 text: Optional[AutoMapperTextInputType],
                 family: Optional[AutoMapperTextInputType]
                 ) -> None:
        super().__init__()
        self.value = dict()
        if use:
            self.value["use"] = AutoMapperValueParser.parse_value(use)
        if text:
            self.value["text"] = AutoMapperValueParser.parse_value(text)
        if family:
            self.value["family"] = AutoMapperValueParser.parse_value(family)
