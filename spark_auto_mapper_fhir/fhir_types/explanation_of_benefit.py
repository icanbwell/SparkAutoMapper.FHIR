from typing import Optional, Union

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.accident_backbone_element import FhirAccidentBackboneElement
from spark_auto_mapper_fhir.fhir_types.add_item_backbone_element import FhirAddItemBackboneElement
from spark_auto_mapper_fhir.fhir_types.adjudication import AutoMapperFhirDataTypeAdjudication
from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.benefit_balance import FhirBenefitBalance
from spark_auto_mapper_fhir.fhir_types.care_team_backbone_element import FhirCareTeamBackboneElement
from spark_auto_mapper_fhir.fhir_types.claim import FhirClaim
from spark_auto_mapper_fhir.fhir_types.claim_response import FhirClaimResponse
from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.diagnosis_backbone_element import AutoMapperFhirDataTypeDiagnosisBackboneElement
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier
from spark_auto_mapper_fhir.fhir_types.insurance_backbone_element import AutoMapperFhirDataTypeInsuranceBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import AutoMapperFhirDataTypeLocation
from spark_auto_mapper_fhir.fhir_types.medication_request import AutoMapperFhirDataTypeMedicationRequest
from spark_auto_mapper_fhir.fhir_types.note import FhirNote
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.patient import AutoMapperFhirDataTypePatient
from spark_auto_mapper_fhir.fhir_types.payee_backbone_element import AutoMapperFhirDataTypePayeeBackboneElement
from spark_auto_mapper_fhir.fhir_types.payment_backbone_element import AutoMapperFhirDataTypePaymentBackboneElement
from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.practitioner import AutoMapperFhirDataTypePractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import AutoMapperFhirDataTypePractitionerRole
from spark_auto_mapper_fhir.fhir_types.procedure_backbone_element import AutoMapperFhirDataTypeProcedureBackboneElement
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.revenue_item_backbone_element import \
    AutoMapperFhirDataTypeRevenueItemBackboneElement
from spark_auto_mapper_fhir.fhir_types.service_request import FhirServiceRequest
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.supporting_info_backbone_element import \
    AutoMapperFhirDataTypeSupportingInfoBackboneElement
from spark_auto_mapper_fhir.fhir_types.total_backbone_element import AutoMapperFhirDataTypeTotalBackBoneElement
from spark_auto_mapper_fhir.fhir_types.vision_prescription import AutoMapperFhirDataTypeVisionPrescription


class AutoMapperFhirDataTypeExplanationOfBenefit(AutoMapperDataTypeComplexBase):
    # noinspection SpellCheckingInspection,PyPep8Naming
    @classmethod
    def map(cls,
            status: AutoMapperFhirCodeInputType,
            type_: AutoMapperFhirDataTypeCodeableConcept,
            use: AutoMapperFhirCodeInputType,
            patient: AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypePatient],
            created: AutoMapperDateInputType,
            insurer: AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeOrganization],
            insurance: FhirList[AutoMapperFhirDataTypeInsuranceBackboneElement],
            outcome: AutoMapperFhirCodeInputType,
            enterer: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole
                ]
            ]] = None,
            provider: Optional[FhirList[
                AutoMapperFhirDataTypeReference[
                    Union[
                        AutoMapperFhirDataTypeOrganization,
                        AutoMapperFhirDataTypePractitioner,
                        AutoMapperFhirDataTypePractitionerRole
                    ]
                ]
            ]] = None,
            billablePeriod: Optional[AutoMapperFhirDataTypePeriod] = None,
            subType: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            identifier: Optional[FhirList[AutoMapperFhirDataTypeIdentifier]] = None,
            priority: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            prescription: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypeMedicationRequest,
                    AutoMapperFhirDataTypeVisionPrescription
                ]
            ]] = None,
            originalPrescription: Optional[AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypeMedicationRequest
                ]
            ]] = None,
            payee: Optional[AutoMapperFhirDataTypePayeeBackboneElement] = None,
            referral: Optional[AutoMapperFhirDataTypeReference[FhirServiceRequest]] = None,
            facility: Optional[AutoMapperFhirDataTypeLocation] = None,
            claim: Optional[AutoMapperFhirDataTypeReference[FhirClaim]] = None,
            claimResponse: Optional[AutoMapperFhirDataTypeReference[FhirClaimResponse]] = None,
            disposition: Optional[FhirString] = None,
            preAuthRef: Optional[FhirList[FhirString]] = None,
            preAuthRefPeriod: Optional[FhirList[AutoMapperFhirDataTypePeriod]] = None,
            careTeam: Optional[FhirList[FhirCareTeamBackboneElement]] = None,
            supportingInfo: Optional[FhirList[AutoMapperFhirDataTypeSupportingInfoBackboneElement]] = None,
            diagnosis: Optional[FhirList[AutoMapperFhirDataTypeDiagnosisBackboneElement]] = None,
            procedure: Optional[FhirList[AutoMapperFhirDataTypeProcedureBackboneElement]] = None,
            precedence: Optional[AutoMapperFhirPositiveIntInputType] = None,
            accident: Optional[FhirAccidentBackboneElement] = None,
            item: Optional[FhirList[AutoMapperFhirDataTypeRevenueItemBackboneElement]] = None,
            addItem: Optional[FhirList[FhirAddItemBackboneElement]] = None,
            adjudication: Optional[AutoMapperFhirDataTypeAdjudication] = None,
            total: Optional[FhirList[AutoMapperFhirDataTypeTotalBackBoneElement]] = None,
            payment: Optional[AutoMapperFhirDataTypePaymentBackboneElement] = None,
            formCode: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            form: Optional[FhirAttachment] = None,
            processNote: Optional[FhirNote] = None,
            benefitPeriod: Optional[AutoMapperFhirDataTypePeriod] = None,
            benefitBalance: Optional[FhirList[FhirBenefitBalance]] = None
            ) -> 'AutoMapperFhirDataTypeExplanationOfBenefit':
        """
        ExplanationOfBenefit Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ExplanationOfBenefit
        Explanation of Benefit resource

        :param status: active | cancelled | draft | entered-in-error.
                        https://hl7.org/FHIR/valueset-explanationofbenefit-status.html
        :param type_: Category or discipline. https://hl7.org/FHIR/valueset-claim-type.html
        :param use: claim | preauthorization | predetermination. https://hl7.org/FHIR/valueset-claim-use.html
        :param patient: The recipient of the products and services
        :param created: Response creation date
        :param insurer: Party responsible for reimbursement
        :param insurance: Patient insurance information
        :param outcome: queued | complete | error | partial. https://hl7.org/FHIR/valueset-remittance-outcome.html

        :param enterer: Author of the claim
        :param provider: Party responsible for the claim
        :param billablePeriod: Relevant time frame for the claim
        :param subType: More granular claim type. https://hl7.org/FHIR/valueset-claim-subtype.html
        :param identifier: Business Identifier for the resource
        :param priority: Desired processing urgency. http://terminology.hl7.org/CodeSystem/processpriority
        :param prescription: Prescription authorizing services or products
        :param originalPrescription: Original prescription if superceded by fulfiller
        :param payee: Recipient of benefits payable
        :param referral: Treatment Referral
        :param facility: Servicing Facility
        :param claim: Claim reference
        :param claimResponse: Claim response reference
        :param disposition: Disposition Message
        :param preAuthRef: Preauthorization reference
        :param preAuthRefPeriod: Preauthorization in-effect period
        :param careTeam: Care Team members
        :param supportingInfo: Supporting information
        :param diagnosis: Pertinent diagnosis information
        :param procedure: Clinical procedures performed
        :param precedence: Precedence (primary, secondary, etc.)
        :param accident: Details of the event
        :param item: Product or service provided
        :param addItem: Insurer added line items
        :param adjudication: Header-level adjudication
        :param total: Adjudication totals
        :param payment: Payment Details
        :param formCode: Printed form identifier.  https://hl7.org/FHIR/valueset-forms.html
        :param form: Printed reference or actual form
        :param processNote: Note concerning adjudication
        :param benefitPeriod: When the benefits are applicable
        :param benefitBalance: Balance by Benefit Category
        """
        return AutoMapperFhirDataTypeExplanationOfBenefit(
            status=status,
            type_=type_,
            use=use,
            patient=patient,
            created=created,
            insurer=insurer,
            insurance=insurance,
            outcome=outcome,
            enterer=enterer,
            provider=provider,
            billablePeriod=billablePeriod,
            subType=subType,
            identifier=identifier,
            priority=priority,
            prescription=prescription,
            originalPrescription=originalPrescription,
            payee=payee,
            referral=referral,
            facility=facility,
            claim=claim,
            claimResponse=claimResponse,
            disposition=disposition,
            preAuthRef=preAuthRef,
            preAuthRefPeriod=preAuthRefPeriod,
            careTeam=careTeam,
            supportingInfo=supportingInfo,
            diagnosis=diagnosis,
            procedure=procedure,
            precedence=precedence,
            accident=accident,
            item=item,
            addItem=addItem,
            adjudication=adjudication,
            total=total,
            payment=payment,
            formCode=formCode,
            form=form,
            processNote=processNote,
            benefitPeriod=benefitPeriod,
            benefitBalance=benefitBalance
        )
