from typing import Optional

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Address(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        use: Optional[FhirString] = None,
        type_: Optional[FhirString] = None,
        text: Optional[FhirString] = None,
        line: Optional[FhirList[FhirString]] = None,
        city: Optional[FhirString] = None,
        district: Optional[FhirString] = None,
        state: Optional[FhirString] = None,
        postalCode: Optional[FhirString] = None,
        country: Optional[FhirString] = None,
        period: Optional[Period] = None
    ):
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
        super().__init__(
            id_=id_,
            extension=extension,
            use=use,
            type=type_,
            text=text,
            line=line,
            city=city,
            district=district,
            state=state,
            postalCode=postalCode,
            country=country,
            period=period
        )
