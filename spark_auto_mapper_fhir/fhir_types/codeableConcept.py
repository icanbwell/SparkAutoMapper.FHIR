from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.coding import FhirCoding
from spark_auto_mapper_fhir.fhir_types.string import FhirString


# noinspection SpellCheckingInspection
class FhirCodeableConcept(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            coding: Optional[FhirCoding] = None,
            text: Optional[FhirString] = None
            ) -> 'FhirCodeableConcept':
        """
        CodeableConcept Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CodeableConcept


        :param coding: Code defined by a terminology system
        :param text: Plain text representation of the concept
        """
        return FhirCodeableConcept(
            coding=coding,
            text=text
        )
