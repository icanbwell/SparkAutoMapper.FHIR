from typing import Optional, TypeVar, Generic

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

_T = TypeVar("_T")


class FhirReference(Generic[_T], FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        reference: Optional[FhirString] = None,
        type_: Optional[FhirUri] = None,
        identifier: Optional[FhirIdentifier] = None,
        display: Optional[FhirString] = None
    ) -> 'FhirReference[_T]':
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
