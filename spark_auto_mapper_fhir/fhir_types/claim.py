from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.accident_backbone_element import FhirAccidentBackboneElement
from spark_auto_mapper_fhir.fhir_types.care_team_backbone_element import FhirCareTeamBackboneElement
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.device_request import FhirDeviceRequest
from spark_auto_mapper_fhir.fhir_types.diagnosis_backbone_element import FhirDiagnosisBackboneElement
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.insurance_backbone_element import FhirInsuranceBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.medication_request import FhirMedicationRequest
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.payee_backbone_element import FhirPayeeBackboneElement
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.procedure_backbone_element import FhirProcedureBackboneElement
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_claim_backbone_element import FhirRelatedClaimBackboneElement
from spark_auto_mapper_fhir.fhir_types.revenue_item_backbone_element import FhirRevenueItemBackboneElement
from spark_auto_mapper_fhir.fhir_types.service_request import FhirServiceRequest
from spark_auto_mapper_fhir.fhir_types.supporting_info_backbone_element import FhirSupportingInfoBackboneElement
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_sub_type import FhirClaimSubTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_type import FhirClaimTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_use import FhirClaimUseCode
from spark_auto_mapper_fhir.fhir_types.valuesets.financial_resource_status import FhirFinancialResourceStatusCode
from spark_auto_mapper_fhir.fhir_types.valuesets.funds_reservation import FhirFundsReservationCode
from spark_auto_mapper_fhir.fhir_types.valuesets.process_priority import FhirProcessPriorityCode
from spark_auto_mapper_fhir.fhir_types.vision_prescription import FhirVisionPrescription


class FhirClaim(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(
        cls,
        status: FhirFinancialResourceStatusCode,
        type_: FhirCodeableConcept[FhirClaimTypeCode],
        use: FhirClaimUseCode,
        patient: FhirReference[FhirPatient],
        created: FhirDateTime,
        provider: FhirReference[Union[FhirPractitioner, FhirPractitionerRole,
                                      FhirOrganization]],
        priority: FhirCodeableConcept[FhirProcessPriorityCode],
        insurance: FhirList[FhirInsuranceBackboneElement],
        id_: Optional[FhirId] = None,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        subType: Optional[FhirCodeableConcept[FhirClaimSubTypeCode]] = None,
        billablePeriod: Optional[FhirPeriod] = None,
        enterer: Optional[FhirReference[Union[FhirPractitioner,
                                              FhirPractitionerRole]]] = None,
        insurer: Optional[FhirReference[FhirOrganization]] = None,
        fundsReserve: Optional[FhirCodeableConcept[FhirFundsReservationCode]
                               ] = None,
        related: Optional[FhirList[FhirRelatedClaimBackboneElement]] = None,
        prescription: Optional[FhirReference[Union[FhirDeviceRequest,
                                                   FhirMedicationRequest,
                                                   FhirVisionPrescription]]
                               ] = None,
        originalPrescription: Optional[FhirReference[
            Union[FhirDeviceRequest, FhirMedicationRequest,
                  FhirVisionPrescription]]] = None,
        payee: Optional[FhirPayeeBackboneElement] = None,
        referral: Optional[FhirReference[FhirServiceRequest]] = None,
        facility: Optional[FhirReference[FhirLocation]] = None,
        careTeam: Optional[FhirList[FhirCareTeamBackboneElement]] = None,
        supportingInfo: Optional[FhirList[FhirSupportingInfoBackboneElement]
                                 ] = None,
        diagnosis: Optional[FhirList[FhirDiagnosisBackboneElement]] = None,
        procedure: Optional[FhirList[FhirProcedureBackboneElement]] = None,
        accident: Optional[FhirAccidentBackboneElement] = None,
        item: Optional[FhirList[FhirRevenueItemBackboneElement]] = None,
        total: Optional[FhirMoney] = None
    ) -> 'FhirClaim':
        """
        Claim Resource in FHIR
        https://hl7.org/FHIR/claim.html
        Claim, Pre-determination or Pre-authorization

        :param id_: id
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
        return FhirClaim(
            id_=id_,
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
            total=total
        )
