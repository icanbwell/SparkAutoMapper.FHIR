from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.communicationrequest import (
    CommunicationRequestSchema,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for replaces
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.request_status import RequestStatus
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.complex_types.communication_request_status_reason import (
        CommunicationRequestStatusReason,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.complex_types.communication_category import (
        CommunicationCategory,
    )
    from spark_auto_mapper_fhir.complex_types.request_priority import RequestPriority
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for medium
    from spark_auto_mapper_fhir.complex_types.communication_medium import (
        CommunicationMedium,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for about
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.backbone_elements.communication_request_payload import (
        CommunicationRequestPayload,
    )
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for recipient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for sender
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.complex_types.communication_reason import (
        CommunicationReason,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CommunicationRequest(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[FhirList[Reference[Union[Resource]]]] = None,
        replaces: Optional[FhirList[Reference[Union[CommunicationRequest]]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        status: RequestStatus,
        statusReason: Optional[
            CodeableConcept[CommunicationRequestStatusReason]
        ] = None,
        category: Optional[FhirList[CodeableConcept[CommunicationCategory]]] = None,
        priority: Optional[RequestPriority] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        medium: Optional[FhirList[CodeableConcept[CommunicationMedium]]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        about: Optional[FhirList[Reference[Union[Resource]]]] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        payload: Optional[FhirList[CommunicationRequestPayload]] = None,
        authoredOn: Optional[FhirDateTime] = None,
        requester: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    Patient,
                    RelatedPerson,
                    Device,
                ]
            ]
        ] = None,
        recipient: Optional[
            FhirList[
                Reference[
                    Union[
                        Device,
                        Organization,
                        Patient,
                        Practitioner,
                        PractitionerRole,
                        RelatedPerson,
                        Group,
                        CareTeam,
                        HealthcareService,
                    ]
                ]
            ]
        ] = None,
        sender: Optional[
            Reference[
                Union[
                    Device,
                    Organization,
                    Patient,
                    Practitioner,
                    PractitionerRole,
                    RelatedPerson,
                    HealthcareService,
                ]
            ]
        ] = None,
        reasonCode: Optional[FhirList[CodeableConcept[CommunicationReason]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifiers assigned to this communication request by the performer
        or other systems which remain constant as the resource is updated and
        propagates from server to server.
            :param basedOn: A plan or proposal that is fulfilled in whole or in part by this request.
            :param replaces: Completed or terminated request(s) whose function is taken by this new
        request.
            :param groupIdentifier: A shared identifier common to all requests that were authorized more or less
        simultaneously by a single author, representing the identifier of the
        requisition, prescription or similar form.
            :param status: The status of the proposal or order.
            :param statusReason: Captures the reason for the current state of the CommunicationRequest.
            :param category: The type of message to be sent such as alert, notification, reminder,
        instruction, etc.
            :param priority: Characterizes how quickly the proposed act must be initiated. Includes
        concepts such as stat, urgent, routine.
            :param doNotPerform: If true indicates that the CommunicationRequest is asking for the specified
        action to *not* occur.
            :param medium: A channel that was used for this communication (e.g. email, fax).
            :param subject: The patient or group that is the focus of this communication request.
            :param about: Other resources that pertain to this communication request and to which this
        communication request should be associated.
            :param encounter: The Encounter during which this CommunicationRequest was created or to which
        the creation of this record is tightly associated.
            :param payload: Text, attachment(s), or resource(s) to be communicated to the recipient.
            :param authoredOn: For draft requests, indicates the date of initial creation.  For requests with
        other statuses, indicates the date of activation.
            :param requester: The device, individual, or organization who initiated the request and has
        responsibility for its activation.
            :param recipient: The entity (e.g. person, organization, clinical information system, device,
        group, or care team) which is the intended target of the communication.
            :param sender: The entity (e.g. person, organization, clinical information system, or device)
        which is to be the source of the communication.
            :param reasonCode: Describes why the request is being made in coded or textual form.
            :param reasonReference: Indicates another resource whose existence justifies this request.
            :param note: Comments made about the request by the requester, sender, recipient, subject
        or other participants.
        """
        super().__init__(
            resourceType="CommunicationRequest",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            basedOn=basedOn,
            replaces=replaces,
            groupIdentifier=groupIdentifier,
            status=status,
            statusReason=statusReason,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            medium=medium,
            subject=subject,
            about=about,
            encounter=encounter,
            payload=payload,
            authoredOn=authoredOn,
            requester=requester,
            recipient=recipient,
            sender=sender,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CommunicationRequestSchema.get_schema(
            include_extension=include_extension
        )