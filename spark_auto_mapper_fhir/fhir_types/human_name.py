from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


class AutoMapperFhirDataTypeHumanName(AutoMapperDataTypeComplexBase):
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
