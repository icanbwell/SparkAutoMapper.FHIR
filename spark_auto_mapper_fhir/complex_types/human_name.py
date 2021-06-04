from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.name_use import NameUseCode


class HumanName(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        use: Optional[NameUseCode] = None,
        text: Optional[FhirString] = None,
        family: Optional[FhirString] = None,
        given: Optional[FhirList[FhirString]] = None,
        prefix: Optional[FhirList[FhirString]] = None,
        suffix: Optional[FhirList[FhirString]] = None,
        period: Optional[Period] = None,
    ):
        """
        HumanName Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#HumanName


        :param use: usual | official | temp | nickname | anonymous | old | maiden (https://hl7.org/FHIR/valueset-name-use.html)
        :param text: Text representation of the full name
        :param family: Family name (often called 'Surname')
        :param given: Given names (not always 'first'). Includes middle names
                        This repeating element order: Given Names appear in the correct order for presenting the name
        :param prefix: Parts that come before the name
                        This repeating element order: Prefixes appear in the correct order for presenting the name
        :param suffix: Parts that come after the name
                        This repeating element order: Suffixes appear in the correct order for presenting the name
        :param period: Time period when name was/is in use
        """
        super().__init__(
            id_=id_,
            extension=extension,
            use=use,
            text=text,
            family=family,
            given=given,
            prefix=prefix,
            suffix=suffix,
            period=period,
        )
