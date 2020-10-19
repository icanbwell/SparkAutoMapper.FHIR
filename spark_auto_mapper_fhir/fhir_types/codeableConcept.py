from typing import Optional, TypeVar, Generic

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.coding import FhirCoding
from spark_auto_mapper_fhir.fhir_types.string import FhirString

_T = TypeVar("_T")


# noinspection SpellCheckingInspection
class FhirCodeableConcept(Generic[_T], FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        coding: Optional[FhirCoding[_T]] = None,
        text: Optional[FhirString] = None
    ) -> 'FhirCodeableConcept[_T]':
        """
        CodeableConcept Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CodeableConcept


        :param coding: Code defined by a terminology system
        :param text: Plain text representation of the concept
        """
        return FhirCodeableConcept[_T](coding=coding, text=text)
