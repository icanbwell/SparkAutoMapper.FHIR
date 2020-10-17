# flake8: noqa
# turning off flake8 on this file because of the circular reference
#   Identifier includes Reference which includes Identifier
from typing import Optional, TypeVar, Generic

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

_T = TypeVar("_T")


class FhirReference(Generic[_T], AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            reference: Optional[FhirString] = None,
            type_: Optional[FhirUri] = None,
            # noqa: F821
            identifier: Optional['FhirIdentifier'] = None,  # type: ignore
            display: Optional[FhirString] = None
            ) -> 'FhirReference':
        """
        Reference Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Reference
        A reference from one resource to another
        + Rule: SHALL have a contained resource if a local reference is provided


        :param reference: Literal reference, Relative, internal or absolute URL
        :param type_: Type the reference refers to (e.g. "Patient") (https://hl7.org/FHIR/valueset-resource-types.html)
        :param identifier: Logical reference, when literal reference is not known
        :param display: Text alternative for the resource
        """
        return FhirReference(
            reference=reference,
            type_=type_,
            identifier=identifier,
            display=display
        )
