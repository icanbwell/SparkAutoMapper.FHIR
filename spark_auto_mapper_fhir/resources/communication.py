from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.communication import CommunicationSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for inResponseTo
    from spark_auto_mapper_fhir.complex_types.event_status import EventStatus
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.communicationnotdonereason import (
        Communicationnotdonereason,
    )

    # End Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.communicationcategory import (
        Communicationcategory,
    )

    # End Import for CodeableConcept for category
    from spark_auto_mapper_fhir.complex_types.request_priority import RequestPriority
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.value_sets.communicationtopic import Communicationtopic

    # End Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for about
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
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
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.backbone_elements.communication_payload import (
        CommunicationPayload,
    )
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Communication(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirList[canonical]] = None,
        instantiatesUri: Optional[FhirList[uri]] = None,
        basedOn: Optional[FhirList[Reference[Union[Resource]]]] = None,
        partOf: Optional[FhirList[Reference[Union[Resource]]]] = None,
        inResponseTo: Optional[FhirList[Reference[Union[Communication]]]] = None,
        status: EventStatus,
        statusReason: Optional[CodeableConcept[Communicationnotdonereason]] = None,
        category: Optional[FhirList[CodeableConcept[Communicationcategory]]] = None,
        priority: Optional[RequestPriority] = None,
        medium: Optional[FhirList[CodeableConcept]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        topic: Optional[CodeableConcept[Communicationtopic]] = None,
        about: Optional[FhirList[Reference[Union[Resource]]]] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        sent: Optional[FhirDateTime] = None,
        received: Optional[FhirDateTime] = None,
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
        reasonCode: Optional[FhirList[CodeableConcept]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        payload: Optional[FhirList[CommunicationPayload]] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifiers assigned to this communication by the performer or other
        systems which remain constant as the resource is updated and propagates from
        server to server.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this Communication.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this Communication.
            :param basedOn: An order, proposal or plan fulfilled in whole or in part by this
        Communication.
            :param partOf: Part of this action.
            :param inResponseTo: Prior communication that this communication is in response to.
            :param status: The status of the transmission.
            :param statusReason: Captures the reason for the current state of the Communication.
            :param category: The type of message conveyed such as alert, notification, reminder,
        instruction, etc.
            :param priority: Characterizes how quickly the planned or in progress communication must be
        addressed. Includes concepts such as stat, urgent, routine.
            :param medium: A channel that was used for this communication (e.g. email, fax).
            :param subject: The patient or group that was the focus of this communication.
            :param topic: Description of the purpose/content, similar to a subject line in an email.
            :param about: Other resources that pertain to this communication and to which this
        communication should be associated.
            :param encounter: The Encounter during which this Communication was created or to which the
        creation of this record is tightly associated.
            :param sent: The time when this communication was sent.
            :param received: The time when this communication arrived at the destination.
            :param recipient: The entity (e.g. person, organization, clinical information system, care team
        or device) which was the target of the communication. If receipts need to be
        tracked by an individual, a separate resource instance will need to be created
        for each recipient.  Multiple recipient communications are intended where
        either receipts are not tracked (e.g. a mass mail-out) or a receipt is
        captured in aggregate (all emails confirmed received by a particular time).
            :param sender: The entity (e.g. person, organization, clinical information system, or device)
        which was the source of the communication.
            :param reasonCode: The reason or justification for the communication.
            :param reasonReference: Indicates another resource whose existence justifies this communication.
            :param payload: Text, attachment(s), or resource(s) that was communicated to the recipient.
            :param note: Additional notes or commentary about the communication by the sender, receiver
        or other interested parties.
        """
        super().__init__(
            resourceType="Communication",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            partOf=partOf,
            inResponseTo=inResponseTo,
            status=status,
            statusReason=statusReason,
            category=category,
            priority=priority,
            medium=medium,
            subject=subject,
            topic=topic,
            about=about,
            encounter=encounter,
            sent=sent,
            received=received,
            recipient=recipient,
            sender=sender,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            payload=payload,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CommunicationSchema.get_schema(include_extension=include_extension)
