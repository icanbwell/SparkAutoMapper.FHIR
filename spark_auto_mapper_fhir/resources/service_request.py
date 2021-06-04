from typing import Optional, Union, Any, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.servicerequest import ServiceRequestSchema

from spark_auto_mapper_fhir.backbone_elements.timing_backbone_element import Timing
from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.quantity import Quantity
from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.complex_types.ratio import Ratio
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical, FhirUri
from spark_auto_mapper_fhir.resources.care_plan import CarePlan
from spark_auto_mapper_fhir.resources.care_team import CareTeam
from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.coverage import Coverage
from spark_auto_mapper_fhir.resources.device import Device

from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.resources.specimen import Specimen
from spark_auto_mapper_fhir.valuesets.body_site import SNOMEDCTBodyStructuresCode
from spark_auto_mapper_fhir.valuesets.medication_as_needed_reason import (
    MedicationAsNeededReasonCode,
)
from spark_auto_mapper_fhir.valuesets.participant_role import ParticipantRoleCode
from spark_auto_mapper_fhir.valuesets.procedure_reason import ProcedureReasonCode
from spark_auto_mapper_fhir.valuesets.request_intent import RequestIntentCode
from spark_auto_mapper_fhir.valuesets.request_priority import RequestPriorityCode
from spark_auto_mapper_fhir.valuesets.request_status import RequestStatusCode
from spark_auto_mapper_fhir.valuesets.service_delivery_location_type import (
    ServiceDeliveryLocationTypeCode,
)
from spark_auto_mapper_fhir.valuesets.service_request_category import (
    ServiceRequestCategoryCode,
)
from spark_auto_mapper_fhir.valuesets.service_request_order_detail import (
    ServiceRequestOrderDetailsCode,
)
from spark_auto_mapper_fhir.valuesets.snomed_procedure import SNOMEDCTProcedureCode


class ServiceRequest(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        status: RequestStatusCode,
        intent: RequestIntentCode,
        subject: Reference[Union[Patient, Group, Location, Device]],
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        basedOn: Optional[
            FhirList[Reference[Union[CarePlan, "ServiceRequest", "MedicationRequest"]]]
        ] = None,
        replaces: Optional[FhirList[Reference["ServiceRequest"]]] = None,
        requisition: Optional[Identifier] = None,
        category: Optional[CodeableConcept[ServiceRequestCategoryCode]] = None,
        priority: Optional[RequestPriorityCode] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        code: Optional[CodeableConcept[SNOMEDCTProcedureCode]] = None,
        orderDetail: Optional[
            FhirList[CodeableConcept[ServiceRequestOrderDetailsCode]]
        ] = None,
        quantityQuantity: Optional[Quantity] = None,
        quantityRatio: Optional[Ratio] = None,
        quantityRange: Optional[Range] = None,
        encounter: Optional[Reference[Encounter]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
        asNeededBoolean: Optional[FhirBoolean] = None,
        asNeededCodeableConcept: Optional[
            CodeableConcept[MedicationAsNeededReasonCode]
        ] = None,
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
        performerType: Optional[CodeableConcept[ParticipantRoleCode]] = None,
        performer: Optional[
            FhirList[
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
            ]
        ] = None,
        locationCode: Optional[
            FhirList[CodeableConcept[ServiceDeliveryLocationTypeCode]]
        ] = None,
        locationReference: Optional[FhirList[Reference[Location]]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[ProcedureReasonCode]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        "Condition",
                        "Observation",
                        "DiagnosticReport",
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        insurance: Optional[FhirList[Union[Coverage, ClaimResponse]]] = None,
        supportingInfo: Optional[FhirList[Reference[Any]]] = None,
        specimen: Optional[FhirList[Reference[Specimen]]] = None,
        bodySite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        patientInstruction: Optional[FhirString] = None,
        # relevantHistory: Optional[FhirList[Reference[Provenance]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        ServiceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ServiceRequest
        A request for a service to be performed

        :param id_: id of resource
        :param status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
        :param intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
        :param subject: Individual or Entity the service is ordered for
        :param identifier: Identifiers assigned to this order
        :param instantiatesCanonical: Instantiates FHIR protocol or definition
        :param instantiatesUri: Instantiates external protocol or definition
        :param basedOn: What request fulfills
        :param replaces: What request replaces
        :param requisition: Composite Request ID
        :param category: Classification of service
        :param priority: routine | urgent | asap | stat
        :param doNotPerform: True if service/procedure should not be performed
        :param code: What is being requested/ordered
        :param orderDetail: Additional order information
        :param quantityQuantity: Service amount
        :param quantityRatio: Service amount
        :param quantityRange: Service amount
        :param encounter: Encounter in which the request was created
        :param occurrenceDateTime: What service should occur
        :param occurrencePeriod: What service should occur
        :param occurrenceTiming: What service should occur
        :param asNeededBoolean: Preconditions for service
        :param asNeededCodeableConcept: Preconditions for service
        :param authoredOn: Date request signed
        :param requester: Who/what is requesting service
        :param performerType: Performer role
        :param performer: Requested performer
        :param locationCode: Requested location
        :param locationReference: Requested location
        :param reasonCode: Explanation/Justification for procedure or service
        :param reasonReference: Explanation/Justification for procedure or service
        :param insurance: Associated insurance coverage
        :param supportingInfo: Additional clinical information
        :param specimen: Procedure Samples
        :param bodySite: Location on Body
        :param note: Comments
        :param patientInstruction: Patient or consumer-oriented instructions
        # :param relevantHistory: Request provenance
        """
        super().__init__(
            resourceType="ServiceRequest",
            id_=id_,
            status=status,
            intent=intent,
            subject=subject,
            meta=meta,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            replaces=replaces,
            requisition=requisition,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            code=code,
            orderDetail=orderDetail,
            quantityQuantity=quantityQuantity,
            quantityRatio=quantityRatio,
            quantityRange=quantityRange,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            asNeededBoolean=asNeededBoolean,
            asNeededCodeableConcept=asNeededCodeableConcept,
            authoredOn=authoredOn,
            requester=requester,
            performerType=performerType,
            performer=performer,
            locationCode=locationCode,
            locationReference=locationReference,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            supportingInfo=supportingInfo,
            specimen=specimen,
            bodySite=bodySite,
            note=note,
            patientInstruction=patientInstruction,
            # relevantHistory=relevantHistory,
            extension=extension,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ServiceRequestSchema.get_schema(include_extension=include_extension)
