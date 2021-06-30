from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.devicerequest import DeviceRequestSchema

if TYPE_CHECKING:
    pass
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

    # parameter (DeviceRequest.Parameter)
    from spark_auto_mapper_fhir.backbone_elements.device_request_parameter import (
        DeviceRequestParameter,
    )

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.device import Device

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # authoredOn (dateTime)
    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # performerType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

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

    # codeReference (Reference)
    # Imports for References for codeReference
    # codeCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for codeCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for codeCodeableConcept
    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceRequest(FhirResourceBase):
    """
    DeviceRequest
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        basedOn: Optional[FhirList[Reference[Union[Resource]]]] = None,
        priorRequest: Optional[FhirList[Reference[Union[Resource]]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        status: Optional[RequestStatusCode] = None,
        intent: RequestIntentCode,
        priority: Optional[RequestPriorityCode] = None,
        parameter: Optional[FhirList[DeviceRequestParameter]] = None,
        subject: Reference[Union[Patient, Group, Location, Device]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
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
        codeReference: Optional[Reference[Union[Device]]] = None,
        codeCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
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
            :param parameter: Specific parameters for the ordered item.  For example, the prism value for
        lenses.
            :param subject: The patient who will use the device.
            :param encounter: An encounter that provides additional context in which this request is made.
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
            :param codeReference: None
            :param codeCodeableConcept: None
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
        """
        super().__init__(
            resourceType="DeviceRequest",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            priorRequest=priorRequest,
            groupIdentifier=groupIdentifier,
            status=status,
            intent=intent,
            priority=priority,
            parameter=parameter,
            subject=subject,
            encounter=encounter,
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
            codeReference=codeReference,
            codeCodeableConcept=codeCodeableConcept,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return DeviceRequestSchema.get_schema(include_extension=include_extension)
