from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirHumanName(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            use: Optional[FhirCode] = None,
            text: Optional[FhirString] = None,
            family: Optional[FhirString] = None
            ) -> 'FhirHumanName':
        """
        HumanName Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#HumanName


        :param use: usual | official | temp | nickname | anonymous | old | maiden (https://hl7.org/FHIR/valueset-name-use.html)
        :param text: Text representation of the full name
        :param family: Family name (often called 'Surname')
        """
        return FhirHumanName(
            use=use,
            text=text,
            family=family
        )
