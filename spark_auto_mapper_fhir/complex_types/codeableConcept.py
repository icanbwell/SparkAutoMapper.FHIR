from typing import Optional, TypeVar, Generic

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.fhir_types.string import FhirString

_T = TypeVar("_T")


# noinspection SpellCheckingInspection
class CodeableConcept(Generic[_T], FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        coding: Optional[Coding[_T]] = None,
        text: Optional[FhirString] = None
    ):
        """
        CodeableConcept Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CodeableConcept


        :param coding: Code defined by a terminology system
        :param text: Plain text representation of the concept
        """
        super().__init__(coding=coding, text=text)
