from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


class AutoMapperFhirDataTypeAddress(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            use: Optional[AutoMapperTextInputType] = None,
            type_: Optional[AutoMapperTextInputType] = None,
            text: Optional[AutoMapperTextInputType] = None,
            line: Optional[AutoMapperDataTypeList] = None,
            city: Optional[AutoMapperTextInputType] = None,
            district: Optional[AutoMapperTextInputType] = None,
            state: Optional[AutoMapperTextInputType] = None,
            postalCode: Optional[AutoMapperTextInputType] = None,
            country: Optional[AutoMapperTextInputType] = None
            ) -> 'AutoMapperFhirDataTypeAddress':
        """
        Address Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Address


        :param use: usual | official | temp | nickname | anonymous | old | maiden (https://hl7.org/FHIR/valueset-name-use.html)
        :param type_: postal | physical | both (https://hl7.org/FHIR/valueset-address-type.html)
        :param text: Text representation of the full name
        :param line: Street name, number, direction & P.O. Box etc.
                This repeating element order: The order in which lines should appear in an address label
        :param city: Name of city, town etc.
        :param district: District name (aka county)
        :param state: Sub-unit of country (abbreviations ok)
        :param postalCode: 	Postal code for area
        :param country: Country (e.g. can be ISO 3166 2 or 3 letter code)
        """
        return AutoMapperFhirDataTypeAddress(
            use=use,
            type=type_,
            text=text,
            line=line,
            city=city,
            district=district,
            state=state,
            postalCode=postalCode,
            country=country
        )
