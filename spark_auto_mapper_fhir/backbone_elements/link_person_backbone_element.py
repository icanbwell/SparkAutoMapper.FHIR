from typing import Union, Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.resources.patient import Patient
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.person import Person
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.identity_assurance_level import (
    IdentityAssuranceLevelCode,
)


class LinkPersonBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        target: Reference[Union[Patient, Practitioner, RelatedPerson, "Person"]],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        assurance: Optional[IdentityAssuranceLevelCode] = None,
    ) -> None:
        """
        LinkPersonBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/person-definitions.html#Person.link
        Link to a resource that concerns the same actual person


        :param target: The resource to which this actual person is associated
        :param assurance: level1 | level2 | level3 | level4
        """
        super().__init__(
            id_=id_, extension=extension, target=target, assurance=assurance
        )
