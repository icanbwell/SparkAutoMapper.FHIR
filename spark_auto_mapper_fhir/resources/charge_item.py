from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.chargeitem import ChargeItemSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # definitionUri (uri)
    # definitionCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # status (ChargeItemStatus)
    from spark_auto_mapper_fhir.value_sets.charge_item_status import (
        ChargeItemStatusCode,
    )

    # partOf (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.charge_item_code import ChargeItemCodeCode

    # End Import for CodeableConcept for code
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # context (Reference)
    # Imports for References for context
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare

    # performer (ChargeItem.Performer)
    from spark_auto_mapper_fhir.backbone_elements.charge_item_performer import (
        ChargeItemPerformer,
    )

    # performingOrganization (Reference)
    # Imports for References for performingOrganization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # requestingOrganization (Reference)
    # Imports for References for requestingOrganization
    # costCenter (Reference)
    # Imports for References for costCenter
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # bodysite (CodeableConcept)
    # Import for CodeableConcept for bodysite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodysite
    # factorOverride (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # priceOverride (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # overrideReason (string)
    # enterer (Reference)
    # Imports for References for enterer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # enteredDate (dateTime)
    # reason (CodeableConcept)
    # Import for CodeableConcept for reason
    from spark_auto_mapper_fhir.value_sets.icd_10_codes import ICD_10CodesCode

    # End Import for CodeableConcept for reason
    # service (Reference)
    # Imports for References for service
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.imaging_study import ImagingStudy
    from spark_auto_mapper_fhir.resources.immunization import Immunization
    from spark_auto_mapper_fhir.resources.medication_administration import (
        MedicationAdministration,
    )
    from spark_auto_mapper_fhir.resources.medication_dispense import MedicationDispense
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.supply_delivery import SupplyDelivery

    # account (Reference)
    # Imports for References for account
    from spark_auto_mapper_fhir.resources.account import Account

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # supportingInformation (Reference)
    # Imports for References for supportingInformation
    from spark_auto_mapper_fhir.resources.resource import Resource

    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # productReference (Reference)
    # Imports for References for productReference
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance

    # productCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for productCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for productCodeableConcept


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ChargeItem(FhirResourceBase):
    """
    ChargeItem
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        definitionUri: Optional[FhirList[FhirUri]] = None,
        definitionCanonical: Optional[FhirList[FhirCanonical]] = None,
        status: ChargeItemStatusCode,
        partOf: Optional[FhirList[Reference[Union[ChargeItem]]]] = None,
        code: CodeableConcept[ChargeItemCodeCode],
        subject: Reference[Union[Patient, Group]],
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        performer: Optional[FhirList[ChargeItemPerformer]] = None,
        performingOrganization: Optional[Reference[Union[Organization]]] = None,
        requestingOrganization: Optional[Reference[Union[Organization]]] = None,
        costCenter: Optional[Reference[Union[Organization]]] = None,
        quantity: Optional[Quantity] = None,
        bodysite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        factorOverride: Optional[FhirDecimal] = None,
        priceOverride: Optional[Money] = None,
        overrideReason: Optional[FhirString] = None,
        enterer: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    Patient,
                    Device,
                    RelatedPerson,
                ]
            ]
        ] = None,
        enteredDate: Optional[FhirDateTime] = None,
        reason: Optional[FhirList[CodeableConcept[ICD_10CodesCode]]] = None,
        service: Optional[
            FhirList[
                Reference[
                    Union[
                        DiagnosticReport,
                        ImagingStudy,
                        Immunization,
                        MedicationAdministration,
                        MedicationDispense,
                        Observation,
                        Procedure,
                        SupplyDelivery,
                    ]
                ]
            ]
        ] = None,
        account: Optional[FhirList[Reference[Union[Account]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        supportingInformation: Optional[FhirList[Reference[Union[Resource]]]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
        productReference: Optional[
            Reference[Union[Device, Medication, Substance]]
        ] = None,
        productCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Identifiers assigned to this event performer or other systems.
            :param definitionUri: References the (external) source of pricing information, rules of application
        for the code this ChargeItem uses.
            :param definitionCanonical: References the source of pricing information, rules of application for the
        code this ChargeItem uses.
            :param status: The current state of the ChargeItem.
            :param partOf: ChargeItems can be grouped to larger ChargeItems covering the whole set.
            :param code: A code that identifies the charge, like a billing code.
            :param subject: The individual or set of individuals the action is being or was performed on.
            :param context: The encounter or episode of care that establishes the context for this event.
            :param performer: Indicates who or what performed or participated in the charged service.
            :param performingOrganization: The organization requesting the service.
            :param requestingOrganization: The organization performing the service.
            :param costCenter: The financial cost center permits the tracking of charge attribution.
            :param quantity: Quantity of which the charge item has been serviced.
            :param bodysite: The anatomical location where the related service has been applied.
            :param factorOverride: Factor overriding the factor determined by the rules associated with the code.
            :param priceOverride: Total price of the charge overriding the list price associated with the code.
            :param overrideReason: If the list price or the rule-based factor associated with the code is
        overridden, this attribute can capture a text to indicate the  reason for this
        action.
            :param enterer: The device, practitioner, etc. who entered the charge item.
            :param enteredDate: Date the charge item was entered.
            :param reason: Describes why the event occurred in coded or textual form.
            :param service: Indicated the rendered service that caused this charge.
            :param account: Account into which this ChargeItems belongs.
            :param note: Comments made about the event by the performer, subject or other participants.
            :param supportingInformation: Further information supporting this charge.
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
            :param productReference: None
            :param productCodeableConcept: None
        """
        super().__init__(
            resourceType="ChargeItem",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            definitionUri=definitionUri,
            definitionCanonical=definitionCanonical,
            status=status,
            partOf=partOf,
            code=code,
            subject=subject,
            context=context,
            performer=performer,
            performingOrganization=performingOrganization,
            requestingOrganization=requestingOrganization,
            costCenter=costCenter,
            quantity=quantity,
            bodysite=bodysite,
            factorOverride=factorOverride,
            priceOverride=priceOverride,
            overrideReason=overrideReason,
            enterer=enterer,
            enteredDate=enteredDate,
            reason=reason,
            service=service,
            account=account,
            note=note,
            supportingInformation=supportingInformation,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            productReference=productReference,
            productCodeableConcept=productCodeableConcept,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ChargeItemSchema.get_schema(include_extension=include_extension)
