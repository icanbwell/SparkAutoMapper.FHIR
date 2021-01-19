from typing import Optional, Union, Any, TYPE_CHECKING

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.medicationrequest import MedicationRequestSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.resources.care_plan import CarePlan
from spark_auto_mapper_fhir.resources.care_team import CareTeam
from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.valuesets.condition import ConditionCode
from spark_auto_mapper_fhir.valuesets.medication_request_category import MedicationRequestCategoryCode
from spark_auto_mapper_fhir.valuesets.medication_request_course_of_therapy import \
    MedicationRequestCourseOfTherapyCode
from spark_auto_mapper_fhir.valuesets.medication_request_intent import MedicationRequestIntentCode
from spark_auto_mapper_fhir.valuesets.medication_request_status import MedicationRequestStatusCode
from spark_auto_mapper_fhir.valuesets.medication_request_status_reason import \
    MedicationRequestStatusReasonCode
from spark_auto_mapper_fhir.valuesets.procedure_performer_role import ProcedurePerformerRoleCode
from spark_auto_mapper_fhir.valuesets.request_priority import RequestPriorityCode
if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.coverage import Coverage
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.resources.detected_issue import DetectedIssue
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.backbone_elements.dispense_request_backbone_element import \
    DispenseRequestBackboneElement
from spark_auto_mapper_fhir.complex_types.dosage import Dosage
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.resources.immunization_recommendation import ImmunizationRecommendation
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.medication_backbone_element import \
    MedicationBackboneElement
if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.backbone_elements.reported_backbone_element import ReportedBackboneElement
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.backbone_elements.substitution_backbone_element import \
    SubstitutionBackboneElement


class MedicationRequest(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        status: MedicationRequestStatusCode,
        intent: MedicationRequestIntentCode,
        medication: MedicationBackboneElement,
        subject: Reference[Union[Patient, Group]],
        id_: FhirId,
        meta: Optional[Meta] = None,
        statusReason: Optional[
            CodeableConcept[MedicationRequestStatusReasonCode]] = None,
        category: Optional[FhirList[
            CodeableConcept[MedicationRequestCategoryCode]]] = None,
        priority: Optional[RequestPriorityCode] = None,
        reported: Optional[ReportedBackboneElement] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        encounter: Optional[Encounter] = None,
        supportingInformation: Optional[FhirList[Any]] = None,
        authoredOn: Optional[FhirDateTime] = None,
        requester: Optional[Reference[Union[Practitioner, PractitionerRole,
                                            Organization, Patient,
                                            RelatedPerson, Device]]] = None,
        performer: Optional[Reference[Union[Practitioner, PractitionerRole,
                                            Organization, Patient,
                                            RelatedPerson, Device,
                                            CareTeam]]] = None,
        performerType: Optional[CodeableConcept[ProcedurePerformerRoleCode]
                                ] = None,
        recorder: Optional[Reference[Union[Practitioner,
                                           PractitionerRole]]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[ConditionCode]]] = None,
        reasonReference: Optional[FhirList[Reference[Union['Condition',
                                                           'Observation']]]
                                  ] = None,
        basedOn: Optional[FhirList[Union[CarePlan, 'MedicationRequest',
                                         ServiceRequest,
                                         ImmunizationRecommendation]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        courseOfTherapyType: Optional[
            CodeableConcept[MedicationRequestCourseOfTherapyCode]] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage,
                                                     ClaimResponse]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        dosageInstruction: Optional[FhirList[Dosage]] = None,
        dispenseRequest: Optional[DispenseRequestBackboneElement] = None,
        substitution: Optional[SubstitutionBackboneElement] = None,
        priorPrescription: Optional[Reference['MedicationRequest']] = None,
        detectedIssue: Optional[FhirList[Reference[DetectedIssue]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        MedicationRequest Resource in FHIR
        https://hl7.org/FHIR/medicationrequest.html
        Ordering of medication for patient or group

        :param status: active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown.
                https://hl7.org/FHIR/valueset-medicationrequest-status.html
        :param intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
                        https://hl7.org/FHIR/valueset-medicationrequest-intent.html
        :param medication: Medication to be taken. https://hl7.org/FHIR/valueset-medication-codes.html

        :param id_: id of resource
        :param statusReason: Reason for current status.
                            https://hl7.org/FHIR/valueset-medicationrequest-status-reason.html
        :param category: Type of medication usage. https://hl7.org/FHIR/valueset-medicationrequest-category.html
        :param priority: 	routine | urgent | asap | stat. https://hl7.org/FHIR/valueset-request-priority.html
        :param reported: Reported rather than primary record
        :param subject: Who or group medication request is for
        :param identifier: External ids for this request
        :param encounter: 	Encounter created as part of encounter/admission/stay
        :param supportingInformation: Information to support ordering of the medication
        :param authoredOn: 	When request was initially authored
        :param requester: Who/What requested the Request
        :param performer: Intended performer of administration
        :param performerType: 	Desired kind of performer of the medication administration.
                                https://hl7.org/FHIR/valueset-performer-role.html
        :param recorder: Person who entered the request
        :param reasonCode: 	Reason or indication for ordering or not ordering the medication.
                            https://hl7.org/FHIR/valueset-condition-code.html
        :param reasonReference: Condition or observation that supports why the prescription is being written
        :param basedOn: What request fulfills
        :param groupIdentifier: Composite request this is part of
        :param courseOfTherapyType: Overall pattern of medication administration.
                                    https://hl7.org/FHIR/valueset-medicationrequest-course-of-therapy.html
        :param insurance: Associated insurance coverage
        :param note: Information about the prescription
        :param dosageInstruction: How the medication should be taken
        :param dispenseRequest: Medication supply authorization
        :param substitution: Any restrictions on medication substitution
        :param priorPrescription: An order/prescription that is being replaced
        :param detectedIssue: Clinical Issue with action
        """
        super().__init__(
            resourceType="MedicationRequest",
            id_=id_,
            meta=meta,
            extension=extension,
            status=status,
            intent=intent,
            medication=medication,
            statusReason=statusReason,
            category=category,
            priority=priority,
            reported=reported,
            subject=subject,
            identifier=identifier,
            encounter=encounter,
            supportingInformation=supportingInformation,
            authoredOn=authoredOn,
            requester=requester,
            performer=performer,
            performerType=performerType,
            recorder=recorder,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            basedOn=basedOn,
            groupIdentifier=groupIdentifier,
            courseOfTherapyType=courseOfTherapyType,
            insurance=insurance,
            note=note,
            dosageInstruction=dosageInstruction,
            dispenseRequest=dispenseRequest,
            substitution=substitution,
            priorPrescription=priorPrescription,
            detectedIssue=detectedIssue
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return MedicationRequestSchema.get_schema(
            include_extension=include_extension
        )
