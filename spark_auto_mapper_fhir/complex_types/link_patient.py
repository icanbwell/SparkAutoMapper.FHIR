from typing import Union, Any, Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.link_type import LinkTypeCode


class LinkPatient(FhirComplexTypeBase):
    def __init__(
        self,
        other: Reference[Union[Any, RelatedPerson]],
        type_: LinkTypeCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ):
        """
        LinkPatient Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#LinkPatient
        Link to another patient resource that concerns the same actual person


        :param other: The other patient or related person resource that the link refers to
        :param type_: replaced-by | replaces | refer | seealso. https://hl7.org/FHIR/valueset-link-type.html
        """
        super().__init__(id_=id_, extension=extension, other=other, type_=type_)
