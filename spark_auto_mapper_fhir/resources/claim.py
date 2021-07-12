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
from spark_fhir_schemas.r4.resources.claim import ClaimSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (FinancialResourceStatusCodes)
    from spark_auto_mapper_fhir.value_sets.financial_resource_status_codes import (
        FinancialResourceStatusCodesCode,
    )

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.claim_type_codes import ClaimTypeCodesCode

    # End Import for CodeableConcept for type_
    # subType (CodeableConcept)
    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.example_claim_sub_type_codes import (
        ExampleClaimSubTypeCodesCode,
    )

    # End Import for CodeableConcept for subType
    # use (Use)
    from spark_auto_mapper_fhir.value_sets.use import UseCode

    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # billablePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # created (dateTime)
    # enterer (Reference)
    # Imports for References for enterer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # insurer (Reference)
    # Imports for References for insurer
    from spark_auto_mapper_fhir.resources.organization import Organization

    # provider (Reference)
    # Imports for References for provider
    # priority (CodeableConcept)
    # Import for CodeableConcept for priority
    from spark_auto_mapper_fhir.value_sets.process_priority_codes import (
        ProcessPriorityCodesCode,
    )

    # End Import for CodeableConcept for priority
    # fundsReserve (CodeableConcept)
    # Import for CodeableConcept for fundsReserve
    from spark_auto_mapper_fhir.value_sets.funds_reservation_codes import (
        FundsReservationCodesCode,
    )

    # End Import for CodeableConcept for fundsReserve
    # related (Claim.Related)
    from spark_auto_mapper_fhir.backbone_elements.claim_related import ClaimRelated

    # prescription (Reference)
    # Imports for References for prescription
    from spark_auto_mapper_fhir.resources.device_request import DeviceRequest
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.vision_prescription import VisionPrescription

    # originalPrescription (Reference)
    # Imports for References for originalPrescription
    # payee (Claim.Payee)
    from spark_auto_mapper_fhir.backbone_elements.claim_payee import ClaimPayee

    # referral (Reference)
    # Imports for References for referral
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # facility (Reference)
    # Imports for References for facility
    from spark_auto_mapper_fhir.resources.location import Location

    # careTeam (Claim.CareTeam)
    from spark_auto_mapper_fhir.backbone_elements.claim_care_team import ClaimCareTeam

    # supportingInfo (Claim.SupportingInfo)
    from spark_auto_mapper_fhir.backbone_elements.claim_supporting_info import (
        ClaimSupportingInfo,
    )

    # diagnosis (Claim.Diagnosis)
    from spark_auto_mapper_fhir.backbone_elements.claim_diagnosis import ClaimDiagnosis

    # procedure (Claim.Procedure)
    from spark_auto_mapper_fhir.backbone_elements.claim_procedure import ClaimProcedure

    # insurance (Claim.Insurance)
    from spark_auto_mapper_fhir.backbone_elements.claim_insurance import ClaimInsurance

    # accident (Claim.Accident)
    from spark_auto_mapper_fhir.backbone_elements.claim_accident import ClaimAccident

    # item (Claim.Item)
    from spark_auto_mapper_fhir.backbone_elements.claim_item import ClaimItem

    # total (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Claim(FhirResourceBase):
    """
    Claim
    claim.xsd
        A provider issued list of professional services and products which have been
    provided, or are to be provided, to a patient which is sent to an insurer for
    reimbursement.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: FinancialResourceStatusCodesCode,
        type_: CodeableConcept[ClaimTypeCodesCode],
        subType: Optional[CodeableConcept[ExampleClaimSubTypeCodesCode]] = None,
        use: UseCode,
        patient: Reference[Patient],
        billablePeriod: Optional[Period] = None,
        created: FhirDateTime,
        enterer: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        insurer: Optional[Reference[Organization]] = None,
        provider: Reference[Union[Practitioner, PractitionerRole, Organization]],
        priority: CodeableConcept[ProcessPriorityCodesCode],
        fundsReserve: Optional[CodeableConcept[FundsReservationCodesCode]] = None,
        related: Optional[FhirList[ClaimRelated]] = None,
        prescription: Optional[
            Reference[Union[DeviceRequest, MedicationRequest, VisionPrescription]]
        ] = None,
        originalPrescription: Optional[
            Reference[Union[DeviceRequest, MedicationRequest, VisionPrescription]]
        ] = None,
        payee: Optional[ClaimPayee] = None,
        referral: Optional[Reference[ServiceRequest]] = None,
        facility: Optional[Reference[Location]] = None,
        careTeam: Optional[FhirList[ClaimCareTeam]] = None,
        supportingInfo: Optional[FhirList[ClaimSupportingInfo]] = None,
        diagnosis: Optional[FhirList[ClaimDiagnosis]] = None,
        procedure: Optional[FhirList[ClaimProcedure]] = None,
        insurance: FhirList[ClaimInsurance],
        accident: Optional[ClaimAccident] = None,
        item: Optional[FhirList[ClaimItem]] = None,
        total: Optional[Money] = None,
    ) -> None:
        """
            A provider issued list of professional services and products which have been
        provided, or are to be provided, to a patient which is sent to an insurer for
        reimbursement.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: A unique identifier assigned to this claim.
            :param status: The status of the resource instance.
            :param type_: The category of claim, e.g. oral, pharmacy, vision, institutional,
        professional.
            :param subType: A finer grained suite of claim type codes which may convey additional
        information such as Inpatient vs Outpatient and/or a specialty service.
            :param use: A code to indicate whether the nature of the request is: to request
        adjudication of products and services previously rendered; or requesting
        authorization and adjudication for provision in the future; or requesting the
        non-binding adjudication of the listed products and services which could be
        provided in the future.
            :param patient: The party to whom the professional services and/or products have been supplied
        or are being considered and for whom actual or forecast reimbursement is
        sought.
            :param billablePeriod: The period for which charges are being submitted.
            :param created: The date this resource was created.
            :param enterer: Individual who created the claim, predetermination or preauthorization.
            :param insurer: The Insurer who is target of the request.
            :param provider: The provider which is responsible for the claim, predetermination or
        preauthorization.
            :param priority: The provider-required urgency of processing the request. Typical values
        include: stat, routine deferred.
            :param fundsReserve: A code to indicate whether and for whom funds are to be reserved for future
        claims.
            :param related: Other claims which are related to this claim such as prior submissions or
        claims for related services or for the same event.
            :param prescription: Prescription to support the dispensing of pharmacy, device or vision products.
            :param originalPrescription: Original prescription which has been superseded by this prescription to
        support the dispensing of pharmacy services, medications or products.
            :param payee: The party to be reimbursed for cost of the products and services according to
        the terms of the policy.
            :param referral: A reference to a referral resource.
            :param facility: Facility where the services were provided.
            :param careTeam: The members of the team who provided the products and services.
            :param supportingInfo: Additional information codes regarding exceptions, special considerations, the
        condition, situation, prior or concurrent issues.
            :param diagnosis: Information about diagnoses relevant to the claim items.
            :param procedure: Procedures performed on the patient relevant to the billing items with the
        claim.
            :param insurance: Financial instruments for reimbursement for the health care products and
        services specified on the claim.
            :param accident: Details of an accident which resulted in injuries which required the products
        and services listed in the claim.
            :param item: A claim line. Either a simple  product or service or a 'group' of details
        which can each be a simple items or groups of sub-details.
            :param total: The total value of the all the items in the claim.
        """
        super().__init__(
            resourceType="Claim",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
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
            fundsReserve=fundsReserve,
            related=related,
            prescription=prescription,
            originalPrescription=originalPrescription,
            payee=payee,
            referral=referral,
            facility=facility,
            careTeam=careTeam,
            supportingInfo=supportingInfo,
            diagnosis=diagnosis,
            procedure=procedure,
            insurance=insurance,
            accident=accident,
            item=item,
            total=total,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ClaimSchema.get_schema(include_extension=include_extension)
