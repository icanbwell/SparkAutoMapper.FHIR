from typing import Optional, Union, Any

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList

from spark_auto_mapper_fhir.fhir_types.annotation import FhirAnnotation
from spark_auto_mapper_fhir.fhir_types.care_plan import FhirCarePlan
from spark_auto_mapper_fhir.fhir_types.care_team import AutoMapperFhirDataTypeCareTeam
from spark_auto_mapper_fhir.fhir_types.claim_response import FhirClaimResponse
from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.condition import AutoMapperFhirDataTypeCondition
from spark_auto_mapper_fhir.fhir_types.coverage import AutoMapperFhirDataTypeCoverage
from spark_auto_mapper_fhir.fhir_types.date_time import AutoMapperFhirDateTimeType
from spark_auto_mapper_fhir.fhir_types.detected_issue import FhirDetectedIssue
from spark_auto_mapper_fhir.fhir_types.device import AutoMapperFhirDataTypeDevice
from spark_auto_mapper_fhir.fhir_types.dispense_request_backbone_element import \
    AutoMapperFhirDataTypeDispenseRequestBackboneElement
from spark_auto_mapper_fhir.fhir_types.dosage import AutoMapperFhirDataTypeDosage
from spark_auto_mapper_fhir.fhir_types.encounter import AutoMapperFhirDataTypeEncounter
from spark_auto_mapper_fhir.fhir_types.group import AutoMapperFhirDataTypeGroup
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier
from spark_auto_mapper_fhir.fhir_types.immunization_recommendation import FhirImmunizationRecommendation
from spark_auto_mapper_fhir.fhir_types.medication_backbone_element import \
    AutoMapperFhirDataTypeMedicationBackboneElement
from spark_auto_mapper_fhir.fhir_types.observation import AutoMapperFhirDataTypeObservation
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.patient import AutoMapperFhirDataTypePatient
from spark_auto_mapper_fhir.fhir_types.practitioner import AutoMapperFhirDataTypePractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import AutoMapperFhirDataTypePractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.related_person import AutoMapperFhirDataTypeRelatedPerson
from spark_auto_mapper_fhir.fhir_types.reported_backbone_element import AutoMapperFhirDataTypeReportedBackboneElement
from spark_auto_mapper_fhir.fhir_types.service_request import FhirServiceRequest
from spark_auto_mapper_fhir.fhir_types.substitution_backbone_element import \
    AutoMapperFhirDataTypeSubstitutionBackboneElement


class AutoMapperFhirDataTypeMedicationRequest(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            status: AutoMapperFhirCodeInputType,
            intent: AutoMapperFhirCodeInputType,
            medication: AutoMapperFhirDataTypeMedicationBackboneElement,
            statusReason: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            category: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            priority: Optional[AutoMapperFhirCodeInputType] = None,
            reported: Optional[AutoMapperFhirDataTypeReportedBackboneElement] = None,
            subject: AutoMapperFhirDataTypeReference[
                Union[AutoMapperFhirDataTypePatient, AutoMapperFhirDataTypeGroup]
            ] = None,
            identifier: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeIdentifier]] = None,
            encounter: Optional[AutoMapperFhirDataTypeEncounter] = None,
            supportingInformation: Optional[AutoMapperDataTypeList[Any]] = None,
            authoredOn: Optional[AutoMapperFhirDateTimeType] = None,
            requester: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole,
                    AutoMapperFhirDataTypeOrganization,
                    AutoMapperFhirDataTypePatient,
                    AutoMapperFhirDataTypeRelatedPerson,
                    AutoMapperFhirDataTypeDevice
                ]
            ]] = None,
            performer: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole,
                    AutoMapperFhirDataTypeOrganization,
                    AutoMapperFhirDataTypePatient,
                    AutoMapperFhirDataTypeRelatedPerson,
                    AutoMapperFhirDataTypeDevice,
                    AutoMapperFhirDataTypeCareTeam
                ]
            ]] = None,
            performerType: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            recorder: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole
                ]
            ]] = None,
            reasonCode: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            reasonReference: Optional[AutoMapperDataTypeList[
                AutoMapperFhirDataTypeReference[
                    Union[
                        AutoMapperFhirDataTypeCondition,
                        AutoMapperFhirDataTypeObservation
                    ]
                ]
            ]] = None,
            basedOn: Optional[AutoMapperDataTypeList[
                Union[
                    FhirCarePlan,
                    'AutoMapperFhirDataTypeMedicationRequest',
                    FhirServiceRequest,
                    FhirImmunizationRecommendation
                ]
            ]] = None,
            groupIdentifier: Optional[AutoMapperFhirDataTypeIdentifier] = None,
            courseOfTherapyType: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            insurance: Optional[AutoMapperDataTypeList[
                AutoMapperFhirDataTypeReference[
                    Union[
                        AutoMapperFhirDataTypeCoverage,
                        FhirClaimResponse
                    ]
                ]
            ]] = None,
            note: Optional[AutoMapperDataTypeList[
                FhirAnnotation
            ]] = None,
            dosageInstruction: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeDosage]] = None,
            dispenseRequest: Optional[AutoMapperFhirDataTypeDispenseRequestBackboneElement] = None,
            substitution: Optional[AutoMapperFhirDataTypeSubstitutionBackboneElement] = None,
            priorPrescription: Optional[
                AutoMapperFhirDataTypeReference['AutoMapperFhirDataTypeMedicationRequest']
            ] = None,
            detectedIssue: Optional[AutoMapperDataTypeList[
                AutoMapperFhirDataTypeReference[FhirDetectedIssue]
            ]] = None
            ) -> 'AutoMapperFhirDataTypeMedicationRequest':
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
        return AutoMapperFhirDataTypeMedicationRequest(
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
