from __future__ import annotations
from typing import Optional, Union, List, Any, TYPE_CHECKING

# noinspection PyPackageRequirements
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

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.devicerequest import DeviceRequestSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for priorRequest
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.request_status import RequestStatus
    from spark_auto_mapper_fhir.complex_types.request_intent import RequestIntent
    from spark_auto_mapper_fhir.complex_types.request_priority import RequestPriority
    from spark_auto_mapper_fhir.backbone_elements.device_request_parameter import DeviceRequestParameter
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.participant_roles import ParticipantRolesCode
    # End Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for supportingInfo
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


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
        identifier: Optional[FhirList[Identifier ]] = None,
        instantiatesCanonical: Optional[FhirList[canonical ]] = None,
        instantiatesUri: Optional[FhirList[uri ]] = None,
        basedOn: Optional[FhirList[Reference [Union[Resource]]]] = None,
        priorRequest: Optional[FhirList[Reference [Union[Resource]]]] = None,
        groupIdentifier: Optional[Identifier ] = None,
        status: Optional[RequestStatus ] = None,
        intent: RequestIntent ,
        priority: Optional[RequestPriority ] = None,
        parameter: Optional[FhirList[DeviceRequestParameter ]] = None,
        subject: Reference [Union[Patient, Group, Location, Device]],
        encounter: Optional[Reference [Union[Encounter]]] = None,
        authoredOn: Optional[FhirDateTime ] = None,
        requester: Optional[Reference [Union[Device, Practitioner, PractitionerRole, Organization]]] = None,
        performerType: Optional[CodeableConcept[ParticipantRolesCode] ] = None,
        performer: Optional[Reference [Union[Practitioner, PractitionerRole, Organization, CareTeam, HealthcareService, Patient, Device, RelatedPerson]]] = None,
        reasonCode: Optional[FhirList[CodeableConcept ]] = None,
        reasonReference: Optional[FhirList[Reference [Union[Condition, Observation, DiagnosticReport, DocumentReference]]]] = None,
        insurance: Optional[FhirList[Reference [Union[Coverage, ClaimResponse]]]] = None,
        supportingInfo: Optional[FhirList[Reference [Union[Resource]]]] = None,
        note: Optional[FhirList[Annotation ]] = None,
        relevantHistory: Optional[FhirList[Reference [Union[Provenance]]]] = None,
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
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return DeviceRequestSchema.get_schema(include_extension=include_extension)
