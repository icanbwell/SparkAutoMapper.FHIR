from typing import Optional, TypeVar, Generic, Union

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

_T = TypeVar("_T", bound=Union[FhirResourceBase])


class Reference(FhirComplexTypeBase, Generic[_T]):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        reference: Optional[FhirReference] = None,
        type_: Optional[FhirUri] = None,
        identifier: Optional[Identifier] = None,
        display: Optional[FhirString] = None,
    ):
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
        super().__init__(
            id_=id_,
            extension=extension,
            reference=reference,
            type_=type_,
            identifier=identifier,
            display=display,
        )
