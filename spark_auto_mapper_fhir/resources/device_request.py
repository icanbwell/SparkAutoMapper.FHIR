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
from spark_fhir_schemas.r4.resources.devicerequest import DeviceRequestSchema

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

    # priorRequest (Reference)
    # Imports for References for priorRequest
    # groupIdentifier (Identifier)
    # status (RequestStatus)
    from spark_auto_mapper_fhir.value_sets.request_status import RequestStatusCode

    # intent (RequestIntent)
    from spark_auto_mapper_fhir.value_sets.request_intent import RequestIntentCode

    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # codeReference (Reference)
    # Imports for References for codeReference
    from spark_auto_mapper_fhir.resources.device import Device

    # codeCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for codeCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for codeCodeableConcept
    # parameter (DeviceRequest.Parameter)
    from spark_auto_mapper_fhir.backbone_elements.device_request_parameter import (
        DeviceRequestParameter,
    )

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.location import Location

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # authoredOn (dateTime)
    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # performerType (CodeableConcept)
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.participant_roles import ParticipantRolesCode

    # End Import for CodeableConcept for performerType
    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.condition_or__problem_or__diagnosis_codes import (
        Condition_or_Problem_or_DiagnosisCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # insurance (Reference)
    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse

    # supportingInfo (Reference)
    # Imports for References for supportingInfo
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # relevantHistory (Reference)
    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceRequest(FhirResourceBase):
    """
    DeviceRequest
    devicerequest.xsd
        Represents a request for a patient to employ a medical device. The device may
    be an implantable device, or an external assistive device, such as a walker.
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
        priorRequest: Optional[FhirList[Reference[Union[Resource]]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        status: Optional[RequestStatusCode] = None,
        intent: RequestIntentCode,
        priority: Optional[RequestPriorityCode] = None,
        codeReference: Optional[Reference[Union[Device]]] = None,
        codeCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        parameter: Optional[FhirList[DeviceRequestParameter]] = None,
        subject: Reference[Union[Patient, Group, Location, Device]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
        authoredOn: Optional[FhirDateTime] = None,
        requester: Optional[
            Reference[Union[Device, Practitioner, PractitionerRole, Organization]]
        ] = None,
        performerType: Optional[CodeableConcept[ParticipantRolesCode]] = None,
        performer: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    CareTeam,
                    HealthcareService,
                    Patient,
                    Device,
                    RelatedPerson,
                ]
            ]
        ] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[Condition_or_Problem_or_DiagnosisCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage, ClaimResponse]]]] = None,
        supportingInfo: Optional[FhirList[Reference[Union[Resource]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        relevantHistory: Optional[FhirList[Reference[Union[Provenance]]]] = None,
    ) -> None:
        """
            Represents a request for a patient to employ a medical device. The device may
        be an implantable device, or an external assistive device, such as a walker.
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
            :param identifier: Identifiers assigned to this order by the orderer or by the receiver.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this DeviceRequest.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this DeviceRequest.
            :param basedOn: Plan/proposal/order fulfilled by this request.
            :param priorRequest: The request takes the place of the referenced completed or terminated
        request(s).
            :param groupIdentifier: Composite request this is part of.
            :param status: The status of the request.
            :param intent: Whether the request is a proposal, plan, an original order or a reflex order.
            :param priority: Indicates how quickly the {{title}} should be addressed with respect to other
        requests.
            :param codeReference: None
            :param codeCodeableConcept: None
            :param parameter: Specific parameters for the ordered item.  For example, the prism value for
        lenses.
            :param subject: The patient who will use the device.
            :param encounter: An encounter that provides additional context in which this request is made.
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
            :param authoredOn: When the request transitioned to being actionable.
            :param requester: The individual who initiated the request and has responsibility for its
        activation.
            :param performerType: Desired type of performer for doing the diagnostic testing.
            :param performer: The desired performer for doing the diagnostic testing.
            :param reasonCode: Reason or justification for the use of this device.
            :param reasonReference: Reason or justification for the use of this device.
            :param insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
        determinations that may be required for delivering the requested service.
            :param supportingInfo: Additional clinical information about the patient that may influence the
        request fulfilment.  For example, this may include where on the subject's body
        the device will be used (i.e. the target site).
            :param note: Details about this request that were not represented at all or sufficiently in
        one of the attributes provided in a class. These may include for example a
        comment, an instruction, or a note associated with the statement.
            :param relevantHistory: Key events in the history of the request.
        """
        super().__init__(
            resourceType="DeviceRequest",
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
            priorRequest=priorRequest,
            groupIdentifier=groupIdentifier,
            status=status,
            intent=intent,
            priority=priority,
            codeReference=codeReference,
            codeCodeableConcept=codeCodeableConcept,
            parameter=parameter,
            subject=subject,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            authoredOn=authoredOn,
            requester=requester,
            performerType=performerType,
            performer=performer,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            supportingInfo=supportingInfo,
            note=note,
            relevantHistory=relevantHistory,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return DeviceRequestSchema.get_schema(include_extension=include_extension)
