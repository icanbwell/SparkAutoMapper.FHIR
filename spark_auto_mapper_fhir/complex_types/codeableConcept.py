from typing import Optional, TypeVar, Generic, Union

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase

# https://mypy.readthedocs.io/en/stable/generics.html
_T = TypeVar("_T", bound=Union[FhirValueSetBase])


# noinspection SpellCheckingInspection
class CodeableConcept(FhirComplexTypeBase, Generic[_T]):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        coding: Optional[FhirList[Coding[_T]]] = None,
        text: Optional[FhirString] = None
    ):
        """
        CodeableConcept Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CodeableConcept


        :param coding: Code defined by a terminology system
        :param text: Plain text representation of the concept
        """
        super().__init__(
            id_=id_, extension=extension, coding=coding, text=text
        )
