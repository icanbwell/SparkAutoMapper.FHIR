from typing import Optional, Union, Any

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.annotation import FhirAnnotation
from spark_auto_mapper_fhir.fhir_types.care_plan import FhirCarePlan
from spark_auto_mapper_fhir.fhir_types.care_team import FhirCareTeam
from spark_auto_mapper_fhir.fhir_types.claim_response import FhirClaimResponse
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.condition import FhirConditionCode
from spark_auto_mapper_fhir.fhir_types.valuesets.medication_request_category import FhirMedicationRequestCategoryCode
from spark_auto_mapper_fhir.fhir_types.valuesets.medication_request_course_of_therapy import \
    FhirMedicationRequestCourseOfTherapyCode
from spark_auto_mapper_fhir.fhir_types.valuesets.medication_request_intent import FhirMedicationRequestIntent
from spark_auto_mapper_fhir.fhir_types.valuesets.medication_request_status import FhirMedicationRequestStatusCode
from spark_auto_mapper_fhir.fhir_types.valuesets.medication_request_status_reason import \
    FhirMedicationRequestStatusReasonCode
from spark_auto_mapper_fhir.fhir_types.valuesets.procedure_performer_role import FhirProcedurePerformerRoleCode
from spark_auto_mapper_fhir.fhir_types.valuesets.request_priority import FhirRequestPriorityCode
from spark_auto_mapper_fhir.fhir_types.condition import FhirCondition
from spark_auto_mapper_fhir.fhir_types.coverage import FhirCoverage
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.detected_issue import FhirDetectedIssue
from spark_auto_mapper_fhir.fhir_types.device import FhirDevice
from spark_auto_mapper_fhir.fhir_types.dispense_request_backbone_element import \
    FhirDispenseRequestBackboneElement
from spark_auto_mapper_fhir.fhir_types.dosage import FhirDosage
from spark_auto_mapper_fhir.fhir_types.encounter import FhirEncounter
from spark_auto_mapper_fhir.fhir_types.group import FhirGroup
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.immunization_recommendation import FhirImmunizationRecommendation
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.medication_backbone_element import \
    FhirMedicationBackboneElement
from spark_auto_mapper_fhir.fhir_types.observation import FhirObservation
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_person import FhirRelatedPerson
from spark_auto_mapper_fhir.fhir_types.reported_backbone_element import FhirReportedBackboneElement
from spark_auto_mapper_fhir.fhir_types.service_request import FhirServiceRequest
from spark_auto_mapper_fhir.fhir_types.substitution_backbone_element import \
    FhirSubstitutionBackboneElement


class FhirMedicationRequest(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        status: FhirMedicationRequestStatusCode,
        intent: FhirMedicationRequestIntent,
        medication: FhirMedicationBackboneElement,
        subject: FhirReference[Union[FhirPatient, FhirGroup]],
        statusReason: Optional[
            FhirCodeableConcept[FhirMedicationRequestStatusReasonCode]] = None,
        category: Optional[FhirList[
            FhirCodeableConcept[FhirMedicationRequestCategoryCode]]] = None,
        priority: Optional[FhirRequestPriorityCode] = None,
        reported: Optional[FhirReportedBackboneElement] = None,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        encounter: Optional[FhirEncounter] = None,
        supportingInformation: Optional[FhirList[Any]] = None,
        authoredOn: Optional[FhirDateTime] = None,
        requester: Optional[FhirReference[Union[FhirPractitioner,
                                                FhirPractitionerRole,
                                                FhirOrganization, FhirPatient,
                                                FhirRelatedPerson,
                                                FhirDevice]]] = None,
        performer: Optional[FhirReference[Union[FhirPractitioner,
                                                FhirPractitionerRole,
                                                FhirOrganization, FhirPatient,
                                                FhirRelatedPerson, FhirDevice,
                                                FhirCareTeam]]] = None,
        performerType: Optional[
            FhirCodeableConcept[FhirProcedurePerformerRoleCode]] = None,
        recorder: Optional[FhirReference[Union[FhirPractitioner,
                                               FhirPractitionerRole]]] = None,
        reasonCode: Optional[FhirList[FhirCodeableConcept[FhirConditionCode]]
                             ] = None,
        reasonReference: Optional[FhirList[FhirReference[Union[FhirCondition,
                                                               FhirObservation]
                                                         ]]] = None,
        basedOn: Optional[FhirList[Union[FhirCarePlan, 'FhirMedicationRequest',
                                         FhirServiceRequest,
                                         FhirImmunizationRecommendation]]
                          ] = None,
        groupIdentifier: Optional[FhirIdentifier] = None,
        courseOfTherapyType: Optional[
            FhirCodeableConcept[FhirMedicationRequestCourseOfTherapyCode]
        ] = None,
        insurance: Optional[FhirList[FhirReference[Union[FhirCoverage,
                                                         FhirClaimResponse]]]
                            ] = None,
        note: Optional[FhirList[FhirAnnotation]] = None,
        dosageInstruction: Optional[FhirList[FhirDosage]] = None,
        dispenseRequest: Optional[FhirDispenseRequestBackboneElement] = None,
        substitution: Optional[FhirSubstitutionBackboneElement] = None,
        priorPrescription: Optional[FhirReference['FhirMedicationRequest']
                                    ] = None,
        detectedIssue: Optional[FhirList[FhirReference[FhirDetectedIssue]]
                                ] = None
    ) -> 'FhirMedicationRequest':
        """
        MedicationRequest Resource in FHIR
        https://hl7.org/FHIR/medicationrequest.html
        Ordering of medication for patient or group

        :param status: active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown.
                https://hl7.org/FHIR/valueset-medicationrequest-status.html
        :param intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
                        https://hl7.org/FHIR/valueset-medicationrequest-intent.html
        :param medication: Medication to be taken. https://hl7.org/FHIR/valueset-medication-codes.html
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
        return FhirMedicationRequest(
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
