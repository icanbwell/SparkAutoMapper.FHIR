from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.explanationofbenefit import (
    ExplanationOfBenefitSchema,
)

from spark_auto_mapper_fhir.backbone_elements.accident_backbone_element import (
    AccidentBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefits_add_item_backbone_element import (
    ExplanationOfBenefitsAddItemBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.adjudication_backbone_element import (
    AdjudicationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.care_team_backbone_element import (
    CareTeamBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.diagnosis_backbone_element import (
    DiagnosisBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefits_item_backbone_element import (
    ExplanationOfBenefitsItemBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.insurance_backbone_element import (
    InsuranceBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.payee_backbone_element import (
    PayeeBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.payment_backbone_element import (
    PaymentBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.procedure_backbone_element import (
    ProcedureBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.related_claim_backbone_element import (
    RelatedClaimBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.supporting_info_backbone_element import (
    SupportingInfoBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.total_backbone_element import (
    TotalBackBoneElement,
)
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.complex_types.benefit_balance import BenefitBalance
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.note import Note
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.claim import Claim
from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.resources.vision_prescription import VisionPrescription
from spark_auto_mapper_fhir.valuesets.claim_sub_type import ClaimSubTypeCode
from spark_auto_mapper_fhir.valuesets.claim_type import ClaimTypeCode
from spark_auto_mapper_fhir.valuesets.claim_use import ClaimUseCode
from spark_auto_mapper_fhir.valuesets.explanation_of_benefit_status import (
    ExplanationOfBenefitStatusCode,
)
from spark_auto_mapper_fhir.valuesets.form import FormCode
from spark_auto_mapper_fhir.valuesets.funds_reserve import FundsReserveCode
from spark_auto_mapper_fhir.valuesets.process_priority import ProcessPriorityCode
from spark_auto_mapper_fhir.valuesets.remittance_outcome import RemittanceOutcomeCode


class ExplanationOfBenefit(FhirResourceBase):
    # noinspection SpellCheckingInspection,PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        status: ExplanationOfBenefitStatusCode,
        type_: CodeableConcept[ClaimTypeCode],
        use: ClaimUseCode,
        patient: Reference[Patient],
        created: FhirDate,
        insurer: Reference[Organization],
        provider: Reference[Union[Organization, Practitioner, PractitionerRole]],
        outcome: RemittanceOutcomeCode,
        insurance: FhirList[InsuranceBackboneElement],
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        subType: Optional[CodeableConcept[ClaimSubTypeCode]] = None,
        billablePeriod: Optional[Period] = None,
        enterer: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        priority: Optional[CodeableConcept[ProcessPriorityCode]] = None,
        fundsReserveRequested: Optional[CodeableConcept[FundsReserveCode]] = None,
        fundsReserve: Optional[CodeableConcept[FundsReserveCode]] = None,
        related: Optional[FhirList[RelatedClaimBackboneElement]] = None,
        prescription: Optional[
            Reference[Union[MedicationRequest, VisionPrescription]]
        ] = None,
        originalPrescription: Optional[Reference[Union[MedicationRequest]]] = None,
        payee: Optional[PayeeBackboneElement] = None,
        referral: Optional[Reference[ServiceRequest]] = None,
        facility: Optional[Reference[Location]] = None,
        claim: Optional[Reference[Claim]] = None,
        claimResponse: Optional[Reference[ClaimResponse]] = None,
        disposition: Optional[FhirString] = None,
        preAuthRef: Optional[FhirList[FhirString]] = None,
        preAuthRefPeriod: Optional[FhirList[Period]] = None,
        careTeam: Optional[FhirList[CareTeamBackboneElement]] = None,
        supportingInfo: Optional[FhirList[SupportingInfoBackboneElement]] = None,
        diagnosis: Optional[FhirList[DiagnosisBackboneElement]] = None,
        procedure: Optional[FhirList[ProcedureBackboneElement]] = None,
        precedence: Optional[FhirPositiveInt] = None,
        accident: Optional[AccidentBackboneElement] = None,
        item: Optional[FhirList[ExplanationOfBenefitsItemBackboneElement]] = None,
        addItem: Optional[FhirList[ExplanationOfBenefitsAddItemBackboneElement]] = None,
        adjudication: Optional[AdjudicationBackboneElement] = None,
        total: Optional[FhirList[TotalBackBoneElement]] = None,
        payment: Optional[PaymentBackboneElement] = None,
        formCode: Optional[CodeableConcept[FormCode]] = None,
        form: Optional[Attachment] = None,
        processNote: Optional[FhirList[Note]] = None,
        benefitPeriod: Optional[Period] = None,
        benefitBalance: Optional[FhirList[BenefitBalance]] = None,
    ):
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

        :param id_: id of resource
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
        super().__init__(
            resourceType="ExplanationOfBenefit",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            subType=subType,
            use=use,
            patient=patient,
            billablePeriod=billablePeriod,
            created=created,
            enterer=enterer,
            insurer=insurer,
            provider=provider,
            priority=priority,
            fundsReserveRequested=fundsReserveRequested,
            fundsReserve=fundsReserve,
            related=related,
            prescription=prescription,
            originalPrescription=originalPrescription,
            payee=payee,
            referral=referral,
            facility=facility,
            claim=claim,
            claimResponse=claimResponse,
            outcome=outcome,
            disposition=disposition,
            preAuthRef=preAuthRef,
            preAuthRefPeriod=preAuthRefPeriod,
            careTeam=careTeam,
            supportingInfo=supportingInfo,
            diagnosis=diagnosis,
            procedure=procedure,
            precedence=precedence,
            insurance=insurance,
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
            benefitBalance=benefitBalance,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ExplanationOfBenefitSchema.get_schema(
            include_extension=include_extension
        )
