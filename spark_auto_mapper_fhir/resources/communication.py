from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.communication import CommunicationSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # instantiatesCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # instantiatesUri (uri)
    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource

    # partOf (Reference)
    # Imports for References for partOf
    # inResponseTo (Reference)
    # Imports for References for inResponseTo
    # status (EventStatus)
    from spark_auto_mapper_fhir.value_sets.event_status import EventStatusCode

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.communication_not_done_reason import (
        CommunicationNotDoneReasonCode,
    )

    # End Import for CodeableConcept for statusReason
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.communication_category import (
        CommunicationCategoryCode,
    )

    # End Import for CodeableConcept for category
    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # medium (CodeableConcept)
    # Import for CodeableConcept for medium
    from spark_auto_mapper_fhir.value_sets.participation_mode import ParticipationMode

    # End Import for CodeableConcept for medium
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # topic (CodeableConcept)
    # Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.value_sets.communication_topic import (
        CommunicationTopicCode,
    )

    # End Import for CodeableConcept for topic
    # about (Reference)
    # Imports for References for about
    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # sent (dateTime)
    # received (dateTime)
    # recipient (Reference)
    # Imports for References for recipient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

    # sender (Reference)
    # Imports for References for sender
    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.snomedct_clinical_findings import (
        SNOMEDCTClinicalFindingsCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # payload (Communication.Payload)
    from spark_auto_mapper_fhir.backbone_elements.communication_payload import (
        CommunicationPayload,
    )

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Communication(FhirResourceBase):
    """
    Communication
    communication.xsd
        An occurrence of information being transmitted; e.g. an alert that was sent to
    a responsible provider, a public health agency that was notified about a
    reportable condition.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        basedOn: Optional[FhirList[Reference[Union[Resource]]]] = None,
        partOf: Optional[FhirList[Reference[Union[Resource]]]] = None,
        inResponseTo: Optional[FhirList[Reference[Union[Communication]]]] = None,
        status: EventStatusCode,
        statusReason: Optional[CodeableConcept[CommunicationNotDoneReasonCode]] = None,
        category: Optional[FhirList[CodeableConcept[CommunicationCategoryCode]]] = None,
        priority: Optional[RequestPriorityCode] = None,
        medium: Optional[FhirList[CodeableConcept[ParticipationMode]]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        topic: Optional[CodeableConcept[CommunicationTopicCode]] = None,
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
        reasonCode: Optional[
            FhirList[CodeableConcept[SNOMEDCTClinicalFindingsCode]]
        ] = None,
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
            An occurrence of information being transmitted; e.g. an alert that was sent to
        a responsible provider, a public health agency that was notified about a
        reportable condition.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
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
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
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
