from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.explanationofbenefit import (
    ExplanationOfBenefitSchema,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.explanation_of_benefit_status import (
        ExplanationOfBenefitStatus,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type
    from spark_auto_mapper_fhir.value_sets.claimtypecodes import Claimtypecodes

    # End Import for CodeableConcept for type
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.exampleclaimsubtypecodes import (
        Exampleclaimsubtypecodes,
    )

    # End Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.complex_types.use import Use
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for enterer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for insurer
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for fundsReserveRequested
    from spark_auto_mapper_fhir.value_sets.funds_reservation_codes import (
        FundsReservationCodes,
    )

    # End Import for CodeableConcept for fundsReserveRequested
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for fundsReserve
    from spark_auto_mapper_fhir.value_sets.funds_reservation_codes import (
        FundsReservationCodes,
    )

    # End Import for CodeableConcept for fundsReserve
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_related import (
        ExplanationOfBenefitRelated,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for prescription
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.vision_prescription import VisionPrescription
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for originalPrescription
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_payee import (
        ExplanationOfBenefitPayee,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for referral
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for facility
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for claim
    from spark_auto_mapper_fhir.resources.claim import Claim
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for claimResponse
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse
    from spark_auto_mapper_fhir.complex_types.claim_processing_codes import (
        ClaimProcessingCodes,
    )
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_care_team import (
        ExplanationOfBenefitCareTeam,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_supporting_info import (
        ExplanationOfBenefitSupportingInfo,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_diagnosis import (
        ExplanationOfBenefitDiagnosis,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_procedure import (
        ExplanationOfBenefitProcedure,
    )
    from spark_auto_mapper_fhir.complex_types.positive_int import positiveInt
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_insurance import (
        ExplanationOfBenefitInsurance,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_accident import (
        ExplanationOfBenefitAccident,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_item import (
        ExplanationOfBenefitItem,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_add_item import (
        ExplanationOfBenefitAddItem,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_adjudication import (
        ExplanationOfBenefitAdjudication,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_total import (
        ExplanationOfBenefitTotal,
    )
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_payment import (
        ExplanationOfBenefitPayment,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for formCode
    from spark_auto_mapper_fhir.value_sets.form_codes import FormCodes

    # End Import for CodeableConcept for formCode
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_process_note import (
        ExplanationOfBenefitProcessNote,
    )
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.backbone_elements.explanation_of_benefit_benefit_balance import (
        ExplanationOfBenefitBenefitBalance,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExplanationOfBenefit(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ExplanationOfBenefitStatus,
        type: CodeableConcept[Claimtypecodes],
        subType: Optional[CodeableConcept[Exampleclaimsubtypecodes]] = None,
        use: Use,
        patient: Reference[Union[Patient]],
        billablePeriod: Optional[Period] = None,
        created: FhirDateTime,
        enterer: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        insurer: Reference[Union[Organization]],
        provider: Reference[Union[Practitioner, PractitionerRole, Organization]],
        priority: Optional[CodeableConcept] = None,
        fundsReserveRequested: Optional[CodeableConcept[FundsReservationCodes]] = None,
        fundsReserve: Optional[CodeableConcept[FundsReservationCodes]] = None,
        related: Optional[FhirList[ExplanationOfBenefitRelated]] = None,
        prescription: Optional[
            Reference[Union[MedicationRequest, VisionPrescription]]
        ] = None,
        originalPrescription: Optional[Reference[Union[MedicationRequest]]] = None,
        payee: Optional[ExplanationOfBenefitPayee] = None,
        referral: Optional[Reference[Union[ServiceRequest]]] = None,
        facility: Optional[Reference[Union[Location]]] = None,
        claim: Optional[Reference[Union[Claim]]] = None,
        claimResponse: Optional[Reference[Union[ClaimResponse]]] = None,
        outcome: ClaimProcessingCodes,
        disposition: Optional[FhirString] = None,
        preAuthRef: Optional[FhirList[FhirString]] = None,
        preAuthRefPeriod: Optional[FhirList[Period]] = None,
        careTeam: Optional[FhirList[ExplanationOfBenefitCareTeam]] = None,
        supportingInfo: Optional[FhirList[ExplanationOfBenefitSupportingInfo]] = None,
        diagnosis: Optional[FhirList[ExplanationOfBenefitDiagnosis]] = None,
        procedure: Optional[FhirList[ExplanationOfBenefitProcedure]] = None,
        precedence: Optional[positiveInt] = None,
        insurance: FhirList[ExplanationOfBenefitInsurance],
        accident: Optional[ExplanationOfBenefitAccident] = None,
        item: Optional[FhirList[ExplanationOfBenefitItem]] = None,
        addItem: Optional[FhirList[ExplanationOfBenefitAddItem]] = None,
        adjudication: Optional[FhirList[ExplanationOfBenefitAdjudication]] = None,
        total: Optional[FhirList[ExplanationOfBenefitTotal]] = None,
        payment: Optional[ExplanationOfBenefitPayment] = None,
        formCode: Optional[CodeableConcept[FormCodes]] = None,
        form: Optional[Attachment] = None,
        processNote: Optional[FhirList[ExplanationOfBenefitProcessNote]] = None,
        benefitPeriod: Optional[Period] = None,
        benefitBalance: Optional[FhirList[ExplanationOfBenefitBenefitBalance]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: A unique identifier assigned to this explanation of benefit.
            :param status: The status of the resource instance.
            :param type: The category of claim, e.g. oral, pharmacy, vision, institutional,
        professional.
            :param subType: A finer grained suite of claim type codes which may convey additional
        information such as Inpatient vs Outpatient and/or a specialty service.
            :param use: A code to indicate whether the nature of the request is: to request
        adjudication of products and services previously rendered; or requesting
        authorization and adjudication for provision in the future; or requesting the
        non-binding adjudication of the listed products and services which could be
        provided in the future.
            :param patient: The party to whom the professional services and/or products have been supplied
        or are being considered and for whom actual for forecast reimbursement is
        sought.
            :param billablePeriod: The period for which charges are being submitted.
            :param created: The date this resource was created.
            :param enterer: Individual who created the claim, predetermination or preauthorization.
            :param insurer: The party responsible for authorization, adjudication and reimbursement.
            :param provider: The provider which is responsible for the claim, predetermination or
        preauthorization.
            :param priority: The provider-required urgency of processing the request. Typical values
        include: stat, routine deferred.
            :param fundsReserveRequested: A code to indicate whether and for whom funds are to be reserved for future
        claims.
            :param fundsReserve: A code, used only on a response to a preauthorization, to indicate whether the
        benefits payable have been reserved and for whom.
            :param related: Other claims which are related to this claim such as prior submissions or
        claims for related services or for the same event.
            :param prescription: Prescription to support the dispensing of pharmacy, device or vision products.
            :param originalPrescription: Original prescription which has been superseded by this prescription to
        support the dispensing of pharmacy services, medications or products.
            :param payee: The party to be reimbursed for cost of the products and services according to
        the terms of the policy.
            :param referral: A reference to a referral resource.
            :param facility: Facility where the services were provided.
            :param claim: The business identifier for the instance of the adjudication request: claim
        predetermination or preauthorization.
            :param claimResponse: The business identifier for the instance of the adjudication response: claim,
        predetermination or preauthorization response.
            :param outcome: The outcome of the claim, predetermination, or preauthorization processing.
            :param disposition: A human readable description of the status of the adjudication.
            :param preAuthRef: Reference from the Insurer which is used in later communications which refers
        to this adjudication.
            :param preAuthRefPeriod: The timeframe during which the supplied preauthorization reference may be
        quoted on claims to obtain the adjudication as provided.
            :param careTeam: The members of the team who provided the products and services.
            :param supportingInfo: Additional information codes regarding exceptions, special considerations, the
        condition, situation, prior or concurrent issues.
            :param diagnosis: Information about diagnoses relevant to the claim items.
            :param procedure: Procedures performed on the patient relevant to the billing items with the
        claim.
            :param precedence: This indicates the relative order of a series of EOBs related to different
        coverages for the same suite of services.
            :param insurance: Financial instruments for reimbursement for the health care products and
        services specified on the claim.
            :param accident: Details of a accident which resulted in injuries which required the products
        and services listed in the claim.
            :param item: A claim line. Either a simple (a product or service) or a 'group' of details
        which can also be a simple items or groups of sub-details.
            :param addItem: The first-tier service adjudications for payor added product or service lines.
            :param adjudication: The adjudication results which are presented at the header level rather than
        at the line-item or add-item levels.
            :param total: Categorized monetary totals for the adjudication.
            :param payment: Payment details for the adjudication of the claim.
            :param formCode: A code for the form to be used for printing the content.
            :param form: The actual form, by reference or inclusion, for printing the content or an
        EOB.
            :param processNote: A note that describes or explains adjudication results in a human readable
        form.
            :param benefitPeriod: The term of the benefits documented in this response.
            :param benefitBalance: Balance by Benefit Category.
        """
        super().__init__(
            resourceType="ExplanationOfBenefit",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type=type,
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
