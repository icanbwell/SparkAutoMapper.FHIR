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
from spark_fhir_schemas.r4.resources.adverseevent import AdverseEventSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.adverse_event_actuality import (
        AdverseEventActuality,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.complex_types.adverse_event_category import (
        AdverseEventCategory,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for event
    from spark_auto_mapper_fhir.complex_types.adverse_event_type import AdverseEventType
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for resultingCondition
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for seriousness
    from spark_auto_mapper_fhir.complex_types.adverse_event_seriousness import (
        AdverseEventSeriousness,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for severity
    from spark_auto_mapper_fhir.complex_types.adverse_event_severity import (
        AdverseEventSeverity,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for outcome
    from spark_auto_mapper_fhir.complex_types.adverse_event_outcome import (
        AdverseEventOutcome,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for recorder
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for contributor
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.backbone_elements.adverse_event_suspect_entity import (
        AdverseEventSuspectEntity,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subjectMedicalHistory
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.allergy_intolerance import AllergyIntolerance
    from spark_auto_mapper_fhir.resources.family_member_history import (
        FamilyMemberHistory,
    )
    from spark_auto_mapper_fhir.resources.immunization import Immunization
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.media import Media
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for referenceDocument
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for study
    from spark_auto_mapper_fhir.resources.research_study import ResearchStudy


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AdverseEvent(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        actuality: AdverseEventActuality,
        category: Optional[FhirList[CodeableConcept[AdverseEventCategory]]] = None,
        event: Optional[CodeableConcept[AdverseEventType]] = None,
        subject: Reference[Union[Patient, Group, Practitioner, RelatedPerson]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        date: Optional[FhirDateTime] = None,
        detected: Optional[FhirDateTime] = None,
        recordedDate: Optional[FhirDateTime] = None,
        resultingCondition: Optional[FhirList[Reference[Union[Condition]]]] = None,
        location: Optional[Reference[Union[Location]]] = None,
        seriousness: Optional[CodeableConcept[AdverseEventSeriousness]] = None,
        severity: Optional[CodeableConcept[AdverseEventSeverity]] = None,
        outcome: Optional[CodeableConcept[AdverseEventOutcome]] = None,
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
        referenceDocument: Optional[
            FhirList[Reference[Union[DocumentReference]]]
        ] = None,
        study: Optional[FhirList[Reference[Union[ResearchStudy]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
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
            extension=extension,
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