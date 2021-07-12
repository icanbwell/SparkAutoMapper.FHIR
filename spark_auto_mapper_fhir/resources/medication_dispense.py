from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicationdispense import MedicationDispenseSchema

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

    # partOf (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.procedure import Procedure

    # status (MedicationDispense Status Codes)
    from spark_auto_mapper_fhir.value_sets.medication_dispense_status_codes import (
        MedicationDispenseStatusCodesCode,
    )

    # statusReasonCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReasonCodeableConcept
    from spark_auto_mapper_fhir.value_sets.medication_dispense_status_reason_codes import (
        MedicationDispenseStatusReasonCodesCode,
    )

    # End Import for CodeableConcept for statusReasonCodeableConcept
    # statusReasonReference (Reference)
    # Imports for References for statusReasonReference
    from spark_auto_mapper_fhir.resources.detected_issue import DetectedIssue

    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.medication_dispense_category_codes import (
        MedicationDispenseCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
    # medicationCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for medicationCodeableConcept
    from spark_auto_mapper_fhir.value_sets.snomedct_medication_codes import (
        SNOMEDCTMedicationCodesCode,
    )

    # End Import for CodeableConcept for medicationCodeableConcept
    # medicationReference (Reference)
    # Imports for References for medicationReference
    from spark_auto_mapper_fhir.resources.medication import Medication

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # context (Reference)
    # Imports for References for context
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare

    # supportingInformation (Reference)
    # Imports for References for supportingInformation
    from spark_auto_mapper_fhir.resources.resource import Resource

    # performer (MedicationDispense.Performer)
    from spark_auto_mapper_fhir.backbone_elements.medication_dispense_performer import (
        MedicationDispensePerformer,
    )

    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # authorizingPrescription (Reference)
    # Imports for References for authorizingPrescription
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest

    # type_ (CodeableConcept)
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.act_pharmacy_supply_type import (
        ActPharmacySupplyType,
    )

    # End Import for CodeableConcept for type_
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # daysSupply (Quantity)
    # whenPrepared (dateTime)
    # whenHandedOver (dateTime)
    # destination (Reference)
    # Imports for References for destination
    # receiver (Reference)
    # Imports for References for receiver
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # dosageInstruction (Dosage)
    from spark_auto_mapper_fhir.backbone_elements.dosage import Dosage

    # substitution (MedicationDispense.Substitution)
    from spark_auto_mapper_fhir.backbone_elements.medication_dispense_substitution import (
        MedicationDispenseSubstitution,
    )

    # detectedIssue (Reference)
    # Imports for References for detectedIssue
    # eventHistory (Reference)
    # Imports for References for eventHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationDispense(FhirResourceBase):
    """
    MedicationDispense
    medicationdispense.xsd
        Indicates that a medication product is to be or has been dispensed for a named
    person/patient.  This includes a description of the medication product
    (supply) provided and the instructions for administering the medication.  The
    medication dispense is the result of a pharmacy system responding to a
    medication order.
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
        partOf: Optional[FhirList[Reference[Union[Procedure]]]] = None,
        status: MedicationDispenseStatusCodesCode,
        statusReasonCodeableConcept: Optional[
            CodeableConcept[MedicationDispenseStatusReasonCodesCode]
        ] = None,
        statusReasonReference: Optional[Reference[Union[DetectedIssue]]] = None,
        category: Optional[CodeableConcept[MedicationDispenseCategoryCodesCode]] = None,
        medicationCodeableConcept: Optional[
            CodeableConcept[SNOMEDCTMedicationCodesCode]
        ] = None,
        medicationReference: Optional[Reference[Union[Medication]]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        supportingInformation: Optional[FhirList[Reference[Union[Resource]]]] = None,
        performer: Optional[FhirList[MedicationDispensePerformer]] = None,
        location: Optional[Reference[Union[Location]]] = None,
        authorizingPrescription: Optional[
            FhirList[Reference[Union[MedicationRequest]]]
        ] = None,
        type_: Optional[CodeableConcept[ActPharmacySupplyType]] = None,
        quantity: Optional[Quantity] = None,
        daysSupply: Optional[Quantity] = None,
        whenPrepared: Optional[FhirDateTime] = None,
        whenHandedOver: Optional[FhirDateTime] = None,
        destination: Optional[Reference[Union[Location]]] = None,
        receiver: Optional[FhirList[Reference[Union[Patient, Practitioner]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        dosageInstruction: Optional[FhirList[Dosage]] = None,
        substitution: Optional[MedicationDispenseSubstitution] = None,
        detectedIssue: Optional[FhirList[Reference[Union[DetectedIssue]]]] = None,
        eventHistory: Optional[FhirList[Reference[Union[Provenance]]]] = None,
    ) -> None:
        """
            Indicates that a medication product is to be or has been dispensed for a named
        person/patient.  This includes a description of the medication product
        (supply) provided and the instructions for administering the medication.  The
        medication dispense is the result of a pharmacy system responding to a
        medication order.
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
            :param identifier: Identifiers associated with this Medication Dispense that are defined by
        business processes and/or used to refer to it when a direct URL reference to
        the resource itself is not appropriate. They are business identifiers assigned
        to this resource by the performer or other systems and remain constant as the
        resource is updated and propagates from server to server.
            :param partOf: The procedure that trigger the dispense.
            :param status: A code specifying the state of the set of dispense events.
            :param statusReasonCodeableConcept: None
            :param statusReasonReference: None
            :param category: Indicates the type of medication dispense (for example, where the medication
        is expected to be consumed or administered (i.e. inpatient or outpatient)).
            :param medicationCodeableConcept: None
            :param medicationReference: None
            :param subject: A link to a resource representing the person or the group to whom the
        medication will be given.
            :param context: The encounter or episode of care that establishes the context for this event.
            :param supportingInformation: Additional information that supports the medication being dispensed.
            :param performer: Indicates who or what performed the event.
            :param location: The principal physical location where the dispense was performed.
            :param authorizingPrescription: Indicates the medication order that is being dispensed against.
            :param type_: Indicates the type of dispensing event that is performed. For example, Trial
        Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
            :param quantity: The amount of medication that has been dispensed. Includes unit of measure.
            :param daysSupply: The amount of medication expressed as a timing amount.
            :param whenPrepared: The time when the dispensed product was packaged and reviewed.
            :param whenHandedOver: The time the dispensed product was provided to the patient or their
        representative.
            :param destination: Identification of the facility/location where the medication was shipped to,
        as part of the dispense event.
            :param receiver: Identifies the person who picked up the medication.  This will usually be a
        patient or their caregiver, but some cases exist where it can be a healthcare
        professional.
            :param note: Extra information about the dispense that could not be conveyed in the other
        attributes.
            :param dosageInstruction: Indicates how the medication is to be used by the patient.
            :param substitution: Indicates whether or not substitution was made as part of the dispense.  In
        some cases, substitution will be expected but does not happen, in other cases
        substitution is not expected but does happen.  This block explains what
        substitution did or did not happen and why.  If nothing is specified,
        substitution was not done.
            :param detectedIssue: Indicates an actual or potential clinical issue with or between one or more
        active or proposed clinical actions for a patient; e.g. drug-drug interaction,
        duplicate therapy, dosage alert etc.
            :param eventHistory: A summary of the events of interest that have occurred, such as when the
        dispense was verified.
        """
        super().__init__(
            resourceType="MedicationDispense",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            partOf=partOf,
            status=status,
            statusReasonCodeableConcept=statusReasonCodeableConcept,
            statusReasonReference=statusReasonReference,
            category=category,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            context=context,
            supportingInformation=supportingInformation,
            performer=performer,
            location=location,
            authorizingPrescription=authorizingPrescription,
            type_=type_,
            quantity=quantity,
            daysSupply=daysSupply,
            whenPrepared=whenPrepared,
            whenHandedOver=whenHandedOver,
            destination=destination,
            receiver=receiver,
            note=note,
            dosageInstruction=dosageInstruction,
            substitution=substitution,
            detectedIssue=detectedIssue,
            eventHistory=eventHistory,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicationDispenseSchema.get_schema(include_extension=include_extension)
