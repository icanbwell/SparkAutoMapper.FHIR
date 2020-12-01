from typing import Optional, Union

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.claim import ClaimSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.backbone_elements.accident_backbone_element import AccidentBackboneElement
from spark_auto_mapper_fhir.backbone_elements.care_team_backbone_element import CareTeamBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.resources.device_request import DeviceRequest
from spark_auto_mapper_fhir.backbone_elements.diagnosis_backbone_element import DiagnosisBackboneElement
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.backbone_elements.insurance_backbone_element import InsuranceBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.backbone_elements.payee_backbone_element import PayeeBackboneElement
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.backbone_elements.procedure_backbone_element import ProcedureBackboneElement
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.backbone_elements.related_claim_backbone_element import RelatedClaimBackboneElement
from spark_auto_mapper_fhir.backbone_elements.revenue_item_backbone_element import RevenueItemBackboneElement
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.backbone_elements.supporting_info_backbone_element import SupportingInfoBackboneElement
from spark_auto_mapper_fhir.valuesets.claim_sub_type import ClaimSubTypeCode
from spark_auto_mapper_fhir.valuesets.claim_type import ClaimTypeCode
from spark_auto_mapper_fhir.valuesets.claim_use import ClaimUseCode
from spark_auto_mapper_fhir.valuesets.financial_resource_status import FinancialResourceStatusCode
from spark_auto_mapper_fhir.valuesets.funds_reservation import FundsReservationCode
from spark_auto_mapper_fhir.valuesets.process_priority import ProcessPriorityCode
from spark_auto_mapper_fhir.resources.vision_prescription import VisionPrescription


class Claim(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        status: FinancialResourceStatusCode,
        type_: CodeableConcept[ClaimTypeCode],
        use: ClaimUseCode,
        patient: Reference[Patient],
        created: FhirDateTime,
        provider: Reference[Union[Practitioner, PractitionerRole,
                                  Organization]],
        priority: CodeableConcept[ProcessPriorityCode],
        insurance: FhirList[InsuranceBackboneElement],
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        subType: Optional[CodeableConcept[ClaimSubTypeCode]] = None,
        billablePeriod: Optional[Period] = None,
        enterer: Optional[Reference[Union[Practitioner,
                                          PractitionerRole]]] = None,
        insurer: Optional[Reference[Organization]] = None,
        fundsReserve: Optional[CodeableConcept[FundsReservationCode]] = None,
        related: Optional[FhirList[RelatedClaimBackboneElement]] = None,
        prescription: Optional[Reference[Union[DeviceRequest,
                                               MedicationRequest,
                                               VisionPrescription]]] = None,
        originalPrescription: Optional[Reference[Union[DeviceRequest,
                                                       MedicationRequest,
                                                       VisionPrescription]]
                                       ] = None,
        payee: Optional[PayeeBackboneElement] = None,
        referral: Optional[Reference[ServiceRequest]] = None,
        facility: Optional[Reference[Location]] = None,
        careTeam: Optional[FhirList[CareTeamBackboneElement]] = None,
        supportingInfo: Optional[FhirList[SupportingInfoBackboneElement]
                                 ] = None,
        diagnosis: Optional[FhirList[DiagnosisBackboneElement]] = None,
        procedure: Optional[FhirList[ProcedureBackboneElement]] = None,
        accident: Optional[AccidentBackboneElement] = None,
        item: Optional[FhirList[RevenueItemBackboneElement]] = None,
        total: Optional[Money] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Claim Resource in FHIR
        https://hl7.org/FHIR/claim.html
        Claim, Pre-determination or Pre-authorization

        :param id_: id of resource
        :param status: active | cancelled | draft | entered-in-error. https://hl7.org/FHIR/valueset-fm-status.html
        :param type_: Category or discipline. https://hl7.org/FHIR/valueset-claim-type.html
        :param use: claim | preauthorization | predetermination. https://hl7.org/FHIR/valueset-claim-use.html
        :param patient: The recipient of the products and services
        :param created: Resource creation date
        :param provider: Party responsible for the claim
        :param priority: Desired processing ugency. https://hl7.org/FHIR/valueset-process-priority.html
        :param insurance: Patient insurance information

        :param identifier: Business Identifier for claim
        :param subType: More granular claim type. https://hl7.org/FHIR/valueset-claim-subtype.html
        :param billablePeriod: Relevant time frame for the claim
        :param enterer: Author of the claim
        :param insurer: Target
        :param fundsReserve: For whom to reserve funds. https://hl7.org/FHIR/valueset-fundsreserve.html
        :param related: Prior or corollary claims
        :param prescription: Prescription authorizing services and products
        :param originalPrescription: Original prescription if superseded by fulfiller
        :param payee: Recipient of benefits payable
        :param referral: Treatment referral
        :param facility: Servicing facility
        :param careTeam: Members of the care team
        :param supportingInfo: Supporting information
        :param diagnosis: Pertinent diagnosis information
        :param procedure: Clinical procedures performed
        :param accident: Details of the event
        :param item: Product or service provided
        :param total: Total claim cost
        """
        super().__init__(
            resourceType="Claim",
            id_=id_,
            meta=meta,
            extension=extension,
            status=status,
            type_=type_,
            use=use,
            patient=patient,
            created=created,
            provider=provider,
            priority=priority,
            insurance=insurance,
            identifier=identifier,
            subType=subType,
            billablePeriod=billablePeriod,
            enterer=enterer,
            insurer=insurer,
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
            accident=accident,
            item=item,
            total=total,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ClaimSchema.get_schema(include_extension=include_extension)
