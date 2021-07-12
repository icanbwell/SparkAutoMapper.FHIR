from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.encounter import EncounterSchema

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

    # status (EncounterStatus)
    from spark_auto_mapper_fhir.value_sets.encounter_status import EncounterStatusCode

    # statusHistory (Encounter.StatusHistory)
    from spark_auto_mapper_fhir.backbone_elements.encounter_status_history import (
        EncounterStatusHistory,
    )

    # class_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for class_
    from spark_auto_mapper_fhir.value_sets.act_encounter_code import ActEncounterCode

    # End Import for CodeableConcept for class_
    # classHistory (Encounter.ClassHistory)
    from spark_auto_mapper_fhir.backbone_elements.encounter_class_history import (
        EncounterClassHistory,
    )

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.encounter_type import EncounterTypeCode

    # End Import for CodeableConcept for type_
    # serviceType (CodeableConcept)
    # Import for CodeableConcept for serviceType
    from spark_auto_mapper_fhir.value_sets.service_type import ServiceTypeCode

    # End Import for CodeableConcept for serviceType
    # priority (CodeableConcept)
    # Import for CodeableConcept for priority
    from spark_auto_mapper_fhir.value_sets.act_priority import ActPriority

    # End Import for CodeableConcept for priority
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # episodeOfCare (Reference)
    # Imports for References for episodeOfCare
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare

    # basedOn (Reference)
    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # participant (Encounter.Participant)
    from spark_auto_mapper_fhir.backbone_elements.encounter_participant import (
        EncounterParticipant,
    )

    # appointment (Reference)
    # Imports for References for appointment
    from spark_auto_mapper_fhir.resources.appointment import Appointment

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # length (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.encounter_reason_codes import (
        EncounterReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.immunization_recommendation import (
        ImmunizationRecommendation,
    )

    # diagnosis (Encounter.Diagnosis)
    from spark_auto_mapper_fhir.backbone_elements.encounter_diagnosis import (
        EncounterDiagnosis,
    )

    # account (Reference)
    # Imports for References for account
    from spark_auto_mapper_fhir.resources.account import Account

    # hospitalization (Encounter.Hospitalization)
    from spark_auto_mapper_fhir.backbone_elements.encounter_hospitalization import (
        EncounterHospitalization,
    )

    # location (Encounter.Location)
    from spark_auto_mapper_fhir.backbone_elements.encounter_location import (
        EncounterLocation,
    )

    # serviceProvider (Reference)
    # Imports for References for serviceProvider
    from spark_auto_mapper_fhir.resources.organization import Organization

    # partOf (Reference)
    # Imports for References for partOf


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Encounter(FhirResourceBase):
    """
    Encounter
    encounter.xsd
        An interaction between a patient and healthcare provider(s) for the purpose of
    providing healthcare service(s) or assessing the health status of a patient.
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
        status: EncounterStatusCode,
        statusHistory: Optional[FhirList[EncounterStatusHistory]] = None,
        class_: Coding[ActEncounterCode],
        classHistory: Optional[FhirList[EncounterClassHistory]] = None,
        type_: Optional[FhirList[CodeableConcept[EncounterTypeCode]]] = None,
        serviceType: Optional[CodeableConcept[ServiceTypeCode]] = None,
        priority: Optional[CodeableConcept[ActPriority]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        episodeOfCare: Optional[FhirList[Reference[EpisodeOfCare]]] = None,
        basedOn: Optional[FhirList[Reference[ServiceRequest]]] = None,
        participant: Optional[FhirList[EncounterParticipant]] = None,
        appointment: Optional[FhirList[Reference[Appointment]]] = None,
        period: Optional[Period] = None,
        length: Optional[Duration] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[EncounterReasonCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Procedure, Observation, ImmunizationRecommendation]
                ]
            ]
        ] = None,
        diagnosis: Optional[FhirList[EncounterDiagnosis]] = None,
        account: Optional[FhirList[Reference[Account]]] = None,
        hospitalization: Optional[EncounterHospitalization] = None,
        location: Optional[FhirList[EncounterLocation]] = None,
        serviceProvider: Optional[Reference[Organization]] = None,
        partOf: Optional[Reference[Encounter]] = None,
    ) -> None:
        """
            An interaction between a patient and healthcare provider(s) for the purpose of
        providing healthcare service(s) or assessing the health status of a patient.
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
            :param identifier: Identifier(s) by which this encounter is known.
            :param status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +.
            :param statusHistory: The status history permits the encounter resource to contain the status
        history without needing to read through the historical versions of the
        resource, or even have the server store them.
            :param class_: Concepts representing classification of patient encounter such as ambulatory
        (outpatient), inpatient, emergency, home health or others due to local
        variations.
            :param classHistory: The class history permits the tracking of the encounters transitions without
        needing to go  through the resource history.  This would be used for a case
        where an admission starts of as an emergency encounter, then transitions into
        an inpatient scenario. Doing this and not restarting a new encounter ensures
        that any lab/diagnostic results can more easily follow the patient and not
        require re-processing and not get lost or cancelled during a kind of discharge
        from emergency to inpatient.
            :param type_: Specific type of encounter (e.g. e-mail consultation, surgical day-care,
        skilled nursing, rehabilitation).
            :param serviceType: Broad categorization of the service that is to be provided (e.g. cardiology).
            :param priority: Indicates the urgency of the encounter.
            :param subject: The patient or group present at the encounter.
            :param episodeOfCare: Where a specific encounter should be classified as a part of a specific
        episode(s) of care this field should be used. This association can facilitate
        grouping of related encounters together for a specific purpose, such as
        government reporting, issue tracking, association via a common problem.  The
        association is recorded on the encounter as these are typically created after
        the episode of care and grouped on entry rather than editing the episode of
        care to append another encounter to it (the episode of care could span years).
            :param basedOn: The request this encounter satisfies (e.g. incoming referral or procedure
        request).
            :param participant: The list of people responsible for providing the service.
            :param appointment: The appointment that scheduled this encounter.
            :param period: The start and end time of the encounter.
            :param length: Quantity of time the encounter lasted. This excludes the time during leaves of
        absence.
            :param reasonCode: Reason the encounter takes place, expressed as a code. For admissions, this
        can be used for a coded admission diagnosis.
            :param reasonReference: Reason the encounter takes place, expressed as a code. For admissions, this
        can be used for a coded admission diagnosis.
            :param diagnosis: The list of diagnosis relevant to this encounter.
            :param account: The set of accounts that may be used for billing for this Encounter.
            :param hospitalization: Details about the admission to a healthcare service.
            :param location: List of locations where  the patient has been during this encounter.
            :param serviceProvider: The organization that is primarily responsible for this Encounter's services.
        This MAY be the same as the organization on the Patient record, however it
        could be different, such as if the actor performing the services was from an
        external organization (which may be billed seperately) for an external
        consultation.  Refer to the example bundle showing an abbreviated set of
        Encounters for a colonoscopy.
            :param partOf: Another Encounter of which this encounter is a part of (administratively or in
        time).
        """
        super().__init__(
            resourceType="Encounter",
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
            statusHistory=statusHistory,
            class_=class_,
            classHistory=classHistory,
            type_=type_,
            serviceType=serviceType,
            priority=priority,
            subject=subject,
            episodeOfCare=episodeOfCare,
            basedOn=basedOn,
            participant=participant,
            appointment=appointment,
            period=period,
            length=length,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            diagnosis=diagnosis,
            account=account,
            hospitalization=hospitalization,
            location=location,
            serviceProvider=serviceProvider,
            partOf=partOf,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EncounterSchema.get_schema(include_extension=include_extension)
