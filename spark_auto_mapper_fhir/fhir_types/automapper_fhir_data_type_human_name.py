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

    @classmethod
    def map(cls,
            use: Optional[AutoMapperTextInputType] = None,
            text: Optional[AutoMapperTextInputType] = None,
            family: Optional[AutoMapperTextInputType] = None
            ) -> 'AutoMapperFhirDataTypeHumanName':
        """
        HumanName Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#HumanName


        :param use: usual | official | temp | nickname | anonymous | old | maiden (https://hl7.org/FHIR/valueset-name-use.html)
        :param text: Text representation of the full name
        :param family: Family name (often called 'Surname')
        """
        return AutoMapperFhirDataTypeHumanName(
            use=use,
            text=text,
            family=family
        )
