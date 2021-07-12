from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.researchstudy import ResearchStudySchema

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

    # title (string)
    # protocol (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for protocol
    from spark_auto_mapper_fhir.resources.plan_definition import PlanDefinition

    # partOf (Reference)
    # Imports for References for partOf
    # status (ResearchStudyStatus)
    from spark_auto_mapper_fhir.value_sets.research_study_status import (
        ResearchStudyStatusCode,
    )

    # primaryPurposeType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for primaryPurposeType
    from spark_auto_mapper_fhir.value_sets.research_study_primary_purpose_type import (
        ResearchStudyPrimaryPurposeTypeCode,
    )

    # End Import for CodeableConcept for primaryPurposeType
    # phase (CodeableConcept)
    # Import for CodeableConcept for phase
    from spark_auto_mapper_fhir.value_sets.research_study_phase import (
        ResearchStudyPhaseCode,
    )

    # End Import for CodeableConcept for phase
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for category
    # focus (CodeableConcept)
    # Import for CodeableConcept for focus
    # End Import for CodeableConcept for focus
    # condition (CodeableConcept)
    # Import for CodeableConcept for condition
    from spark_auto_mapper_fhir.value_sets.condition_or__problem_or__diagnosis_codes import (
        Condition_or_Problem_or_DiagnosisCodesCode,
    )

    # End Import for CodeableConcept for condition
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # relatedArtifact (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # keyword (CodeableConcept)
    # Import for CodeableConcept for keyword
    # End Import for CodeableConcept for keyword
    # location (CodeableConcept)
    # Import for CodeableConcept for location
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for location
    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # enrollment (Reference)
    # Imports for References for enrollment
    from spark_auto_mapper_fhir.resources.group import Group

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # sponsor (Reference)
    # Imports for References for sponsor
    from spark_auto_mapper_fhir.resources.organization import Organization

    # principalInvestigator (Reference)
    # Imports for References for principalInvestigator
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # site (Reference)
    # Imports for References for site
    from spark_auto_mapper_fhir.resources.location import Location

    # reasonStopped (CodeableConcept)
    # Import for CodeableConcept for reasonStopped
    from spark_auto_mapper_fhir.value_sets.research_study_reason_stopped import (
        ResearchStudyReasonStoppedCode,
    )

    # End Import for CodeableConcept for reasonStopped
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # arm (ResearchStudy.Arm)
    from spark_auto_mapper_fhir.backbone_elements.research_study_arm import (
        ResearchStudyArm,
    )

    # objective (ResearchStudy.Objective)
    from spark_auto_mapper_fhir.backbone_elements.research_study_objective import (
        ResearchStudyObjective,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResearchStudy(FhirResourceBase):
    """
    ResearchStudy
    researchstudy.xsd
        A process where a researcher or organization plans and then executes a series
    of steps intended to increase the field of healthcare-related knowledge.  This
    includes studies of safety, efficacy, comparative effectiveness and other
    information about medications, devices, therapies and other interventional and
    investigative techniques.  A ResearchStudy involves the gathering of
    information about human or animal subjects.
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
        title: Optional[FhirString] = None,
        protocol: Optional[FhirList[Reference[Union[PlanDefinition]]]] = None,
        partOf: Optional[FhirList[Reference[Union[ResearchStudy]]]] = None,
        status: ResearchStudyStatusCode,
        primaryPurposeType: Optional[
            CodeableConcept[ResearchStudyPrimaryPurposeTypeCode]
        ] = None,
        phase: Optional[CodeableConcept[ResearchStudyPhaseCode]] = None,
        category: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        focus: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        condition: Optional[
            FhirList[CodeableConcept[Condition_or_Problem_or_DiagnosisCodesCode]]
        ] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        relatedArtifact: Optional[FhirList[RelatedArtifact]] = None,
        keyword: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        location: Optional[FhirList[CodeableConcept[JurisdictionValueSetCode]]] = None,
        description: Optional[FhirMarkdown] = None,
        enrollment: Optional[FhirList[Reference[Union[Group]]]] = None,
        period: Optional[Period] = None,
        sponsor: Optional[Reference[Union[Organization]]] = None,
        principalInvestigator: Optional[
            Reference[Union[Practitioner, PractitionerRole]]
        ] = None,
        site: Optional[FhirList[Reference[Union[Location]]]] = None,
        reasonStopped: Optional[CodeableConcept[ResearchStudyReasonStoppedCode]] = None,
        note: Optional[FhirList[Annotation]] = None,
        arm: Optional[FhirList[ResearchStudyArm]] = None,
        objective: Optional[FhirList[ResearchStudyObjective]] = None,
    ) -> None:
        """
            A process where a researcher or organization plans and then executes a series
        of steps intended to increase the field of healthcare-related knowledge.  This
        includes studies of safety, efficacy, comparative effectiveness and other
        information about medications, devices, therapies and other interventional and
        investigative techniques.  A ResearchStudy involves the gathering of
        information about human or animal subjects.
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
            :param identifier: Identifiers assigned to this research study by the sponsor or other systems.
            :param title: A short, descriptive user-friendly label for the study.
            :param protocol: The set of steps expected to be performed as part of the execution of the
        study.
            :param partOf: A larger research study of which this particular study is a component or step.
            :param status: The current state of the study.
            :param primaryPurposeType: The type of study based upon the intent of the study's activities. A
        classification of the intent of the study.
            :param phase: The stage in the progression of a therapy from initial experimental use in
        humans in clinical trials to post-market evaluation.
            :param category: Codes categorizing the type of study such as investigational vs.
        observational, type of blinding, type of randomization, safety vs. efficacy,
        etc.
            :param focus: The medication(s), food(s), therapy(ies), device(s) or other concerns or
        interventions that the study is seeking to gain more information about.
            :param condition: The condition that is the focus of the study.  For example, In a study to
        examine risk factors for Lupus, might have as an inclusion criterion "healthy
        volunteer", but the target condition code would be a Lupus SNOMED code.
            :param contact: Contact details to assist a user in learning more about or engaging with the
        study.
            :param relatedArtifact: Citations, references and other related documents.
            :param keyword: Key terms to aid in searching for or filtering the study.
            :param location: Indicates a country, state or other region where the study is taking place.
            :param description: A full description of how the study is being conducted.
            :param enrollment: Reference to a Group that defines the criteria for and quantity of subjects
        participating in the study.  E.g. " 200 female Europeans between the ages of
        20 and 45 with early onset diabetes".
            :param period: Identifies the start date and the expected (or actual, depending on status)
        end date for the study.
            :param sponsor: An organization that initiates the investigation and is legally responsible
        for the study.
            :param principalInvestigator: A researcher in a study who oversees multiple aspects of the study, such as
        concept development, protocol writing, protocol submission for IRB approval,
        participant recruitment, informed consent, data collection, analysis,
        interpretation and presentation.
            :param site: A facility in which study activities are conducted.
            :param reasonStopped: A description and/or code explaining the premature termination of the study.
            :param note: Comments made about the study by the performer, subject or other participants.
            :param arm: Describes an expected sequence of events for one of the participants of a
        study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
        follow-up.
            :param objective: A goal that the study is aiming to achieve in terms of a scientific question
        to be answered by the analysis of data collected during the study.
        """
        super().__init__(
            resourceType="ResearchStudy",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            title=title,
            protocol=protocol,
            partOf=partOf,
            status=status,
            primaryPurposeType=primaryPurposeType,
            phase=phase,
            category=category,
            focus=focus,
            condition=condition,
            contact=contact,
            relatedArtifact=relatedArtifact,
            keyword=keyword,
            location=location,
            description=description,
            enrollment=enrollment,
            period=period,
            sponsor=sponsor,
            principalInvestigator=principalInvestigator,
            site=site,
            reasonStopped=reasonStopped,
            note=note,
            arm=arm,
            objective=objective,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ResearchStudySchema.get_schema(include_extension=include_extension)
