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
from spark_fhir_schemas.r4.resources.medicationadministration import (
    MedicationAdministrationSchema,
)

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

    # instantiates (uri)
    # partOf (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.procedure import Procedure

    # status (MedicationAdministration Status Codes)
    from spark_auto_mapper_fhir.value_sets.medication_administration_status_codes import (
        MedicationAdministrationStatusCodesCode,
    )

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.snomedct_reason_medication_not_given_codes import (
        SNOMEDCTReasonMedicationNotGivenCodesCode,
    )

    # End Import for CodeableConcept for statusReason
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.medication_administration_category_codes import (
        MedicationAdministrationCategoryCodesCode,
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

    # effectiveDateTime (dateTime)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # performer (MedicationAdministration.Performer)
    from spark_auto_mapper_fhir.backbone_elements.medication_administration_performer import (
        MedicationAdministrationPerformer,
    )

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.reason_medication_given_codes import (
        ReasonMedicationGivenCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport

    # request (Reference)
    # Imports for References for request
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest

    # device (Reference)
    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device import Device

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # dosage (MedicationAdministration.Dosage)
    from spark_auto_mapper_fhir.backbone_elements.medication_administration_dosage import (
        MedicationAdministrationDosage,
    )

    # eventHistory (Reference)
    # Imports for References for eventHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationAdministration(FhirResourceBase):
    """
    MedicationAdministration
    medicationadministration.xsd
        Describes the event of a patient consuming or otherwise being administered a
    medication.  This may be as simple as swallowing a tablet or it may be a long
    running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
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
        instantiates: Optional[FhirList[FhirUri]] = None,
        partOf: Optional[
            FhirList[Reference[Union[MedicationAdministration, Procedure]]]
        ] = None,
        status: MedicationAdministrationStatusCodesCode,
        statusReason: Optional[
            FhirList[CodeableConcept[SNOMEDCTReasonMedicationNotGivenCodesCode]]
        ] = None,
        category: Optional[
            CodeableConcept[MedicationAdministrationCategoryCodesCode]
        ] = None,
        medicationCodeableConcept: Optional[
            CodeableConcept[SNOMEDCTMedicationCodesCode]
        ] = None,
        medicationReference: Optional[Reference[Medication]] = None,
        subject: Reference[Union[Patient, Group]],
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        supportingInformation: Optional[FhirList[Reference[Resource]]] = None,
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        performer: Optional[FhirList[MedicationAdministrationPerformer]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[ReasonMedicationGivenCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[Reference[Union[Condition, Observation, DiagnosticReport]]]
        ] = None,
        request: Optional[Reference[MedicationRequest]] = None,
        device: Optional[FhirList[Reference[Device]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        dosage: Optional[MedicationAdministrationDosage] = None,
        eventHistory: Optional[FhirList[Reference[Provenance]]] = None,
    ) -> None:
        """
            Describes the event of a patient consuming or otherwise being administered a
        medication.  This may be as simple as swallowing a tablet or it may be a long
        running infusion.  Related resources tie this event to the authorizing
        prescription, and the specific encounter between patient and health care
        practitioner.
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
            :param identifier: Identifiers associated with this Medication Administration that are defined by
        business processes and/or used to refer to it when a direct URL reference to
        the resource itself is not appropriate. They are business identifiers assigned
        to this resource by the performer or other systems and remain constant as the
        resource is updated and propagates from server to server.
            :param instantiates: A protocol, guideline, orderset, or other definition that was adhered to in
        whole or in part by this event.
            :param partOf: A larger event of which this particular event is a component or step.
            :param status: Will generally be set to show that the administration has been completed.  For
        some long running administrations such as infusions, it is possible for an
        administration to be started but not completed or it may be paused while some
        other process is under way.
            :param statusReason: A code indicating why the administration was not performed.
            :param category: Indicates where the medication is expected to be consumed or administered.
            :param medicationCodeableConcept: None
            :param medicationReference: None
            :param subject: The person or animal or group receiving the medication.
            :param context: The visit, admission, or other contact between patient and health care
        provider during which the medication administration was performed.
            :param supportingInformation: Additional information (for example, patient height and weight) that supports
        the administration of the medication.
            :param effectiveDateTime: None
            :param effectivePeriod: None
            :param performer: Indicates who or what performed the medication administration and how they
        were involved.
            :param reasonCode: A code indicating why the medication was given.
            :param reasonReference: Condition or observation that supports why the medication was administered.
            :param request: The original request, instruction or authority to perform the administration.
            :param device: The device used in administering the medication to the patient.  For example,
        a particular infusion pump.
            :param note: Extra information about the medication administration that is not conveyed by
        the other attributes.
            :param dosage: Describes the medication dosage information details e.g. dose, rate, site,
        route, etc.
            :param eventHistory: A summary of the events of interest that have occurred, such as when the
        administration was verified.
        """
        super().__init__(
            resourceType="MedicationAdministration",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            instantiates=instantiates,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            category=category,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            context=context,
            supportingInformation=supportingInformation,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            performer=performer,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            request=request,
            device=device,
            note=note,
            dosage=dosage,
            eventHistory=eventHistory,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicationAdministrationSchema.get_schema(
            include_extension=include_extension
        )
