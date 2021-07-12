from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.chargeitem import ChargeItemSchema

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
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
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

    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

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

    # productReference (Reference)
    # Imports for References for productReference
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance

    # productCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for productCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for productCodeableConcept
    # account (Reference)
    # Imports for References for account
    from spark_auto_mapper_fhir.resources.account import Account

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # supportingInformation (Reference)
    # Imports for References for supportingInformation
    from spark_auto_mapper_fhir.resources.resource import Resource


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ChargeItem(FhirResourceBase):
    """
    ChargeItem
    chargeitem.xsd
        The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the product,
    but containing in addition details of the provision, like date, time, amounts
    and participating organizations and persons. Main Usage of the ChargeItem is
    to enable the billing process and internal cost allocation.
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
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        definitionUri: Optional[FhirList[FhirUri]] = None,
        definitionCanonical: Optional[FhirList[FhirCanonical]] = None,
        status: ChargeItemStatusCode,
        partOf: Optional[FhirList[Reference[Union[ChargeItem]]]] = None,
        code: CodeableConcept[ChargeItemCodeCode],
        subject: Reference[Union[Patient, Group]],
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
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
        productReference: Optional[
            Reference[Union[Device, Medication, Substance]]
        ] = None,
        productCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        account: Optional[FhirList[Reference[Union[Account]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        supportingInformation: Optional[FhirList[Reference[Union[Resource]]]] = None,
    ) -> None:
        """
            The resource ChargeItem describes the provision of healthcare provider
        products for a certain patient, therefore referring not only to the product,
        but containing in addition details of the provision, like date, time, amounts
        and participating organizations and persons. Main Usage of the ChargeItem is
        to enable the billing process and internal cost allocation.
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
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
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
            :param productReference: None
            :param productCodeableConcept: None
            :param account: Account into which this ChargeItems belongs.
            :param note: Comments made about the event by the performer, subject or other participants.
            :param supportingInformation: Further information supporting this charge.
        """
        super().__init__(
            resourceType="ChargeItem",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            definitionUri=definitionUri,
            definitionCanonical=definitionCanonical,
            status=status,
            partOf=partOf,
            code=code,
            subject=subject,
            context=context,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
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
            productReference=productReference,
            productCodeableConcept=productCodeableConcept,
            account=account,
            note=note,
            supportingInformation=supportingInformation,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ChargeItemSchema.get_schema(include_extension=include_extension)
