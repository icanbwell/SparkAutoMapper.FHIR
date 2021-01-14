from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.action_participant_role import ActionParticipantRoleCode
from spark_auto_mapper_fhir.valuesets.action_participant_type import ActionParticipantTypeCode


class ParticipantBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: ActionParticipantTypeCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        role: Optional[FhirList[CodeableConcept[ActionParticipantRoleCode]]
                       ] = None
    ) -> None:
        """
        ParticipantBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.action.participant
        Who should participate in the action


        :param type_: patient | practitioner | related-person | device
        :param role: E.g. Nurse, Surgeon, Parent
        """
        super().__init__(id_=id_, extension=extension, type_=type_, role=role)
