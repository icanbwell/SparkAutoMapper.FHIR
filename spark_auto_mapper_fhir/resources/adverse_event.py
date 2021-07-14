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
from spark_fhir_schemas.r4.resources.adverseevent import AdverseEventSchema

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

    # actuality (AdverseEventActuality)
    from spark_auto_mapper_fhir.value_sets.adverse_event_actuality import (
        AdverseEventActualityCode,
    )

    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.adverse_event_category import (
        AdverseEventCategoryCode,
    )

    # End Import for CodeableConcept for category
    # event (CodeableConcept)
    # Import for CodeableConcept for event
    from spark_auto_mapper_fhir.value_sets.snomedct_clinical_findings import (
        SNOMEDCTClinicalFindingsCode,
    )

    # End Import for CodeableConcept for event
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # date (dateTime)
    # detected (dateTime)
    # recordedDate (dateTime)
    # resultingCondition (Reference)
    # Imports for References for resultingCondition
    from spark_auto_mapper_fhir.resources.condition import Condition

    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # seriousness (CodeableConcept)
    # Import for CodeableConcept for seriousness
    from spark_auto_mapper_fhir.value_sets.adverse_event_seriousness import (
        AdverseEventSeriousnessCode,
    )

    # End Import for CodeableConcept for seriousness
    # severity (CodeableConcept)
    # Import for CodeableConcept for severity
    from spark_auto_mapper_fhir.value_sets.adverse_event_severity import (
        AdverseEventSeverityCode,
    )

    # End Import for CodeableConcept for severity
    # outcome (CodeableConcept)
    # Import for CodeableConcept for outcome
    from spark_auto_mapper_fhir.value_sets.adverse_event_outcome import (
        AdverseEventOutcomeCode,
    )

    # End Import for CodeableConcept for outcome
    # recorder (Reference)
    # Imports for References for recorder
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # contributor (Reference)
    # Imports for References for contributor
    from spark_auto_mapper_fhir.resources.device import Device

    # suspectEntity (AdverseEvent.SuspectEntity)
    from spark_auto_mapper_fhir.backbone_elements.adverse_event_suspect_entity import (
        AdverseEventSuspectEntity,
    )

    # subjectMedicalHistory (Reference)
    # Imports for References for subjectMedicalHistory
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.allergy_intolerance import AllergyIntolerance
    from spark_auto_mapper_fhir.resources.family_member_history import (
        FamilyMemberHistory,
    )
    from spark_auto_mapper_fhir.resources.immunization import Immunization
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.media import Media
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # referenceDocument (Reference)
    # Imports for References for referenceDocument
    # study (Reference)
    # Imports for References for study
    from spark_auto_mapper_fhir.resources.research_study import ResearchStudy


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdverseEvent(FhirResourceBase):
    """
    AdverseEvent
    adverseevent.xsd
        Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment, or
    hospitalization, or that results in death.
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
        identifier: Optional[Identifier] = None,
        actuality: AdverseEventActualityCode,
        category: Optional[FhirList[CodeableConcept[AdverseEventCategoryCode]]] = None,
        event: Optional[CodeableConcept[SNOMEDCTClinicalFindingsCode]] = None,
        subject: Reference[Union[Patient, Group, Practitioner, RelatedPerson]],
        encounter: Optional[Reference[Encounter]] = None,
        date: Optional[FhirDateTime] = None,
        detected: Optional[FhirDateTime] = None,
        recordedDate: Optional[FhirDateTime] = None,
        resultingCondition: Optional[FhirList[Reference[Condition]]] = None,
        location: Optional[Reference[Location]] = None,
        seriousness: Optional[CodeableConcept[AdverseEventSeriousnessCode]] = None,
        severity: Optional[CodeableConcept[AdverseEventSeverityCode]] = None,
        outcome: Optional[CodeableConcept[AdverseEventOutcomeCode]] = None,
        recorder: Optional[
            Reference[Union[Patient, Practitioner, PractitionerRole, RelatedPerson]]
        ] = None,
        contributor: Optional[
            FhirList[Reference[Union[Practitioner, PractitionerRole, Device]]]
        ] = None,
        suspectEntity: Optional[FhirList[AdverseEventSuspectEntity]] = None,
        subjectMedicalHistory: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        AllergyIntolerance,
                        FamilyMemberHistory,
                        Immunization,
                        Procedure,
                        Media,
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        referenceDocument: Optional[FhirList[Reference[DocumentReference]]] = None,
        study: Optional[FhirList[Reference[ResearchStudy]]] = None,
    ) -> None:
        """
            Actual or  potential/avoided event causing unintended physical injury
        resulting from or contributed to by medical care, a research study or other
        healthcare setting factors that requires additional monitoring, treatment, or
        hospitalization, or that results in death.
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
            :param identifier: Business identifiers assigned to this adverse event by the performer or other
        systems which remain constant as the resource is updated and propagates from
        server to server.
            :param actuality: Whether the event actually happened, or just had the potential to. Note that
        this is independent of whether anyone was affected or harmed or how severely.
            :param category: The overall type of event, intended for search and filtering purposes.
            :param event: This element defines the specific type of event that occurred or that was
        prevented from occurring.
            :param subject: This subject or group impacted by the event.
            :param encounter: The Encounter during which AdverseEvent was created or to which the creation
        of this record is tightly associated.
            :param date: The date (and perhaps time) when the adverse event occurred.
            :param detected: Estimated or actual date the AdverseEvent began, in the opinion of the
        reporter.
            :param recordedDate: The date on which the existence of the AdverseEvent was first recorded.
            :param resultingCondition: Includes information about the reaction that occurred as a result of exposure
        to a substance (for example, a drug or a chemical).
            :param location: The information about where the adverse event occurred.
            :param seriousness: Assessment whether this event was of real importance.
            :param severity: Describes the severity of the adverse event, in relation to the subject.
        Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but
        a mild heart problem is.
            :param outcome: Describes the type of outcome from the adverse event.
            :param recorder: Information on who recorded the adverse event.  May be the patient or a
        practitioner.
            :param contributor: Parties that may or should contribute or have contributed information to the
        adverse event, which can consist of one or more activities.  Such information
        includes information leading to the decision to perform the activity and how
        to perform the activity (e.g. consultant), information that the activity
        itself seeks to reveal (e.g. informant of clinical history), or information
        about what activity was performed (e.g. informant witness).
            :param suspectEntity: Describes the entity that is suspected to have caused the adverse event.
            :param subjectMedicalHistory: AdverseEvent.subjectMedicalHistory.
            :param referenceDocument: AdverseEvent.referenceDocument.
            :param study: AdverseEvent.study.
        """
        super().__init__(
            resourceType="AdverseEvent",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            actuality=actuality,
            category=category,
            event=event,
            subject=subject,
            encounter=encounter,
            date=date,
            detected=detected,
            recordedDate=recordedDate,
            resultingCondition=resultingCondition,
            location=location,
            seriousness=seriousness,
            severity=severity,
            outcome=outcome,
            recorder=recorder,
            contributor=contributor,
            suspectEntity=suspectEntity,
            subjectMedicalHistory=subjectMedicalHistory,
            referenceDocument=referenceDocument,
            study=study,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AdverseEventSchema.get_schema(include_extension=include_extension)
