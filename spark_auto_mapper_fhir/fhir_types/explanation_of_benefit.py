from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.accident_backbone_element import FhirAccidentBackboneElement
from spark_auto_mapper_fhir.fhir_types.add_item_backbone_element import FhirAddItemBackboneElement
from spark_auto_mapper_fhir.fhir_types.adjudication_backbone_element import FhirAdjudicationBackboneElement
from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.benefit_balance import FhirBenefitBalance
from spark_auto_mapper_fhir.fhir_types.care_team_backbone_element import FhirCareTeamBackboneElement
from spark_auto_mapper_fhir.fhir_types.claim import FhirClaim
from spark_auto_mapper_fhir.fhir_types.claim_response import FhirClaimResponse
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_sub_type import FhirClaimSubTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_type import FhirClaimTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.explanation_of_benefit_status import FhirExplanationOfBenefitStatusCode
from spark_auto_mapper_fhir.fhir_types.valuesets.form import FhirFormCode
from spark_auto_mapper_fhir.fhir_types.valuesets.process_priority import FhirProcessPriorityCode
from spark_auto_mapper_fhir.fhir_types.valuesets.remittance_outcome import FhirRemittanceOutcomeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_use import FhirClaimUseCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.diagnosis_backbone_element import FhirDiagnosisBackboneElement
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.insurance_backbone_element import FhirInsuranceBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.medication_request import FhirMedicationRequest
from spark_auto_mapper_fhir.fhir_types.note import FhirNote
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.payee_backbone_element import FhirPayeeBackboneElement
from spark_auto_mapper_fhir.fhir_types.payment_backbone_element import FhirPaymentBackboneElement
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.procedure_backbone_element import FhirProcedureBackboneElement
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.revenue_item_backbone_element import \
    FhirRevenueItemBackboneElement
from spark_auto_mapper_fhir.fhir_types.service_request import FhirServiceRequest
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.supporting_info_backbone_element import \
    FhirSupportingInfoBackboneElement
from spark_auto_mapper_fhir.fhir_types.total_backbone_element import FhirTotalBackBoneElement
from spark_auto_mapper_fhir.fhir_types.vision_prescription import FhirVisionPrescription


class FhirExplanationOfBenefit(FhirResourceBase):
    # noinspection SpellCheckingInspection,PyPep8Naming
    @classmethod
    def map(
        cls,
        status: FhirExplanationOfBenefitStatusCode,
        type_: FhirCodeableConcept[FhirClaimTypeCode],
        use: FhirClaimUseCode,
        patient: FhirReference[FhirPatient],
        created: FhirDate,
        insurer: FhirReference[FhirOrganization],
        insurance: FhirList[FhirInsuranceBackboneElement],
        outcome: FhirRemittanceOutcomeCode,
        enterer: Optional[FhirReference[Union[FhirPractitioner,
                                              FhirPractitionerRole]]] = None,
        provider: Optional[FhirList[FhirReference[Union[FhirOrganization,
                                                        FhirPractitioner,
                                                        FhirPractitionerRole]]]
                           ] = None,
        billablePeriod: Optional[FhirPeriod] = None,
        subType: Optional[FhirCodeableConcept[FhirClaimSubTypeCode]] = None,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        priority: Optional[FhirCodeableConcept[FhirProcessPriorityCode]
                           ] = None,
        prescription: Optional[FhirReference[Union[FhirMedicationRequest,
                                                   FhirVisionPrescription]]
                               ] = None,
        originalPrescription: Optional[FhirReference[
            Union[FhirMedicationRequest]]] = None,
        payee: Optional[FhirPayeeBackboneElement] = None,
        referral: Optional[FhirReference[FhirServiceRequest]] = None,
        facility: Optional[FhirLocation] = None,
        claim: Optional[FhirReference[FhirClaim]] = None,
        claimResponse: Optional[FhirReference[FhirClaimResponse]] = None,
        disposition: Optional[FhirString] = None,
        preAuthRef: Optional[FhirList[FhirString]] = None,
        preAuthRefPeriod: Optional[FhirList[FhirPeriod]] = None,
        careTeam: Optional[FhirList[FhirCareTeamBackboneElement]] = None,
        supportingInfo: Optional[FhirList[FhirSupportingInfoBackboneElement]
                                 ] = None,
        diagnosis: Optional[FhirList[FhirDiagnosisBackboneElement]] = None,
        procedure: Optional[FhirList[FhirProcedureBackboneElement]] = None,
        precedence: Optional[FhirPositiveInt] = None,
        accident: Optional[FhirAccidentBackboneElement] = None,
        item: Optional[FhirList[FhirRevenueItemBackboneElement]] = None,
        addItem: Optional[FhirList[FhirAddItemBackboneElement]] = None,
        adjudication: Optional[FhirAdjudicationBackboneElement] = None,
        total: Optional[FhirList[FhirTotalBackBoneElement]] = None,
        payment: Optional[FhirPaymentBackboneElement] = None,
        formCode: Optional[FhirCodeableConcept[FhirFormCode]] = None,
        form: Optional[FhirAttachment] = None,
        processNote: Optional[FhirNote] = None,
        benefitPeriod: Optional[FhirPeriod] = None,
        benefitBalance: Optional[FhirList[FhirBenefitBalance]] = None
    ) -> 'FhirExplanationOfBenefit':
        """
        ExplanationOfBenefit Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ExplanationOfBenefit
        Explanation of Benefit resource
        For reporting out to patients or transferring data to patient centered applications,
        such as patient health Record (PHR) application, the ExplanationOfBenefit should be used instead of the
        Claim and ClaimResponse resources as those resources may contain provider and payer specific information
        which is not appropriate for sharing with the patient.

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
        return FhirExplanationOfBenefit(
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
