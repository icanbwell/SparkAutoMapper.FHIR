from __future__ import annotations
from typing import Optional, Union, List, Any, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for type
    from spark_auto_mapper_fhir.value_sets.contract_action_codes import ContractActionCodes
    # End Import for CodeableConcept for type
    from spark_auto_mapper_fhir.backbone_elements.contract_subject import ContractSubject
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for status
    from spark_auto_mapper_fhir.value_sets.contract_resource_action_status_codes import ContractResourceActionStatusCodes
    # End Import for CodeableConcept for status
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for context
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.provenance_participant_type import ProvenanceParticipantType
    # End Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for performerRole
    from spark_auto_mapper_fhir.value_sets.provenance_participant_role import ProvenanceParticipantRole
    # End Import for CodeableConcept for performerRole
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.substance import Substance
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.questionnaire import Questionnaire
    from spark_auto_mapper_fhir.resources.questionnaire_response import QuestionnaireResponse
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractAction(FhirBackboneElementBase):
    """
    """
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        extension: Optional[FhirList[ExtensionBase]] = None,
        doNotPerform: Optional[FhirBoolean ] = None,
        type: CodeableConcept[ContractActionCodes] ,
        subject: Optional[FhirList[ContractSubject ]] = None,
        intent: CodeableConcept ,
        linkId: Optional[FhirList[FhirString ]] = None,
        status: CodeableConcept[ContractResourceActionStatusCodes] ,
        context: Optional[Reference [Union[Encounter, EpisodeOfCare]]] = None,
        contextLinkId: Optional[FhirList[FhirString ]] = None,
        requester: Optional[FhirList[Reference [Union[Patient, RelatedPerson, Practitioner, PractitionerRole, Device, Group, Organization]]]] = None,
        requesterLinkId: Optional[FhirList[FhirString ]] = None,
        performerType: Optional[FhirList[CodeableConcept[ProvenanceParticipantType] ]] = None,
        performerRole: Optional[CodeableConcept[ProvenanceParticipantRole] ] = None,
        performer: Optional[Reference [Union[RelatedPerson, Patient, Practitioner, PractitionerRole, CareTeam, Device, Substance, Organization, Location]]] = None,
        performerLinkId: Optional[FhirList[FhirString ]] = None,
        reasonCode: Optional[FhirList[CodeableConcept ]] = None,
        reasonReference: Optional[FhirList[Reference [Union[Condition, Observation, DiagnosticReport, DocumentReference, Questionnaire, QuestionnaireResponse]]]] = None,
        reason: Optional[FhirList[FhirString ]] = None,
        reasonLinkId: Optional[FhirList[FhirString ]] = None,
        note: Optional[FhirList[Annotation ]] = None,
        securityLabelNumber: Optional[FhirList[unsignedInt ]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param doNotPerform: True if the term prohibits the  action.
        :param type: Activity or service obligation to be done or not done, performed or not
    performed, effectuated or not by this Contract term.
        :param subject: Entity of the action.
        :param intent: Reason or purpose for the action stipulated by this Contract Provision.
        :param linkId: Id [identifier??] of the clause or question text related to this action in the
    referenced form or QuestionnaireResponse.
        :param status: Current state of the term action.
        :param context: Encounter or Episode with primary association to specified term activity.
        :param contextLinkId: Id [identifier??] of the clause or question text related to the requester of
    this action in the referenced form or QuestionnaireResponse.
        :param requester: Who or what initiated the action and has responsibility for its activation.
        :param requesterLinkId: Id [identifier??] of the clause or question text related to the requester of
    this action in the referenced form or QuestionnaireResponse.
        :param performerType: The type of individual that is desired or required to perform or not perform
    the action.
        :param performerRole: The type of role or competency of an individual desired or required to perform
    or not perform the action.
        :param performer: Indicates who or what is being asked to perform (or not perform) the ction.
        :param performerLinkId: Id [identifier??] of the clause or question text related to the reason type or
    reference of this  action in the referenced form or QuestionnaireResponse.
        :param reasonCode: Rationale for the action to be performed or not performed. Describes why the
    action is permitted or prohibited.
        :param reasonReference: Indicates another resource whose existence justifies permitting or not
    permitting this action.
        :param reason: Describes why the action is to be performed or not performed in textual form.
        :param reasonLinkId: Id [identifier??] of the clause or question text related to the reason type or
    reference of this  action in the referenced form or QuestionnaireResponse.
        :param note: Comments made about the term action made by the requester, performer, subject
    or other participants.
        :param securityLabelNumber: Security labels that protects the action.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            doNotPerform=doNotPerform,
            type=type,
            subject=subject,
            intent=intent,
            linkId=linkId,
            status=status,
            context=context,
            contextLinkId=contextLinkId,
            requester=requester,
            requesterLinkId=requesterLinkId,
            performerType=performerType,
            performerRole=performerRole,
            performer=performer,
            performerLinkId=performerLinkId,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            reason=reason,
            reasonLinkId=reasonLinkId,
            note=note,
            securityLabelNumber=securityLabelNumber,
        )
