from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.activitydefinition import ActivityDefinitionSchema

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
    # url (uri)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # version (string)
    # name (string)
    # title (string)
    # subtitle (string)
    # status (PublicationStatus)
    from spark_auto_mapper_fhir.value_sets.publication_status import (
        PublicationStatusCode,
    )

    # experimental (boolean)
    # subjectCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for subjectCodeableConcept
    from spark_auto_mapper_fhir.value_sets.subject_type import SubjectTypeCode

    # End Import for CodeableConcept for subjectCodeableConcept
    # subjectReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subjectReference
    from spark_auto_mapper_fhir.resources.group import Group

    # date (dateTime)
    # publisher (string)
    # contact (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # description (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # useContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # jurisdiction (CodeableConcept)
    # Import for CodeableConcept for jurisdiction
    from spark_auto_mapper_fhir.value_sets.jurisdiction_value_set import (
        JurisdictionValueSetCode,
    )

    # End Import for CodeableConcept for jurisdiction
    # purpose (markdown)
    # usage (string)
    # copyright (markdown)
    # approvalDate (date)
    # lastReviewDate (date)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # topic (CodeableConcept)
    # Import for CodeableConcept for topic
    from spark_auto_mapper_fhir.value_sets.definition_topic import DefinitionTopicCode

    # End Import for CodeableConcept for topic
    # author (ContactDetail)
    # editor (ContactDetail)
    # reviewer (ContactDetail)
    # endorser (ContactDetail)
    # relatedArtifact (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # library (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # kind (RequestResourceType)
    from spark_auto_mapper_fhir.value_sets.request_resource_type import (
        RequestResourceTypeCode,
    )

    # profile (canonical)
    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.procedure_codes_snomedct_ import (
        ProcedureCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for code
    # intent (RequestIntent)
    from spark_auto_mapper_fhir.value_sets.request_intent import RequestIntentCode

    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # doNotPerform (boolean)
    # timingTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # timingDateTime (dateTime)
    # timingAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # timingPeriod (Period)
    # timingRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # timingDuration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # participant (ActivityDefinition.Participant)
    from spark_auto_mapper_fhir.backbone_elements.activity_definition_participant import (
        ActivityDefinitionParticipant,
    )

    # productReference (Reference)
    # Imports for References for productReference
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance

    # productCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for productCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for productCodeableConcept
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # dosage (Dosage)
    from spark_auto_mapper_fhir.backbone_elements.dosage import Dosage

    # bodySite (CodeableConcept)
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # specimenRequirement (Reference)
    # Imports for References for specimenRequirement
    from spark_auto_mapper_fhir.resources.specimen_definition import SpecimenDefinition

    # observationRequirement (Reference)
    # Imports for References for observationRequirement
    from spark_auto_mapper_fhir.resources.observation_definition import (
        ObservationDefinition,
    )

    # observationResultRequirement (Reference)
    # Imports for References for observationResultRequirement
    # transform (canonical)
    # dynamicValue (ActivityDefinition.DynamicValue)
    from spark_auto_mapper_fhir.backbone_elements.activity_definition_dynamic_value import (
        ActivityDefinitionDynamicValue,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActivityDefinition(FhirResourceBase):
    """
    ActivityDefinition
    activitydefinition.xsd
        This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
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
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        status: PublicationStatusCode,
        experimental: Optional[FhirBoolean] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Union[Group]]] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[
            FhirList[CodeableConcept[JurisdictionValueSetCode]]
        ] = None,
        purpose: Optional[FhirMarkdown] = None,
        usage: Optional[FhirString] = None,
        copyright: Optional[FhirMarkdown] = None,
        approvalDate: Optional[FhirDate] = None,
        lastReviewDate: Optional[FhirDate] = None,
        effectivePeriod: Optional[Period] = None,
        topic: Optional[FhirList[CodeableConcept[DefinitionTopicCode]]] = None,
        author: Optional[FhirList[ContactDetail]] = None,
        editor: Optional[FhirList[ContactDetail]] = None,
        reviewer: Optional[FhirList[ContactDetail]] = None,
        endorser: Optional[FhirList[ContactDetail]] = None,
        relatedArtifact: Optional[FhirList[RelatedArtifact]] = None,
        library: Optional[FhirList[FhirCanonical]] = None,
        kind: Optional[RequestResourceTypeCode] = None,
        profile: Optional[FhirCanonical] = None,
        code: Optional[CodeableConcept[ProcedureCodes_SNOMEDCT_Code]] = None,
        intent: Optional[RequestIntentCode] = None,
        priority: Optional[RequestPriorityCode] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        timingTiming: Optional[Timing] = None,
        timingDateTime: Optional[FhirDateTime] = None,
        timingAge: Optional[Age] = None,
        timingPeriod: Optional[Period] = None,
        timingRange: Optional[Range] = None,
        timingDuration: Optional[Duration] = None,
        location: Optional[Reference[Union[Location]]] = None,
        participant: Optional[FhirList[ActivityDefinitionParticipant]] = None,
        productReference: Optional[Reference[Union[Medication, Substance]]] = None,
        productCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        quantity: Optional[Quantity] = None,
        dosage: Optional[FhirList[Dosage]] = None,
        bodySite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        specimenRequirement: Optional[
            FhirList[Reference[Union[SpecimenDefinition]]]
        ] = None,
        observationRequirement: Optional[
            FhirList[Reference[Union[ObservationDefinition]]]
        ] = None,
        observationResultRequirement: Optional[
            FhirList[Reference[Union[ObservationDefinition]]]
        ] = None,
        transform: Optional[FhirCanonical] = None,
        dynamicValue: Optional[FhirList[ActivityDefinitionDynamicValue]] = None,
    ) -> None:
        """
            This resource allows for the definition of some activity to be performed,
        independent of a particular patient, practitioner, or other performance
        context.
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
            :param url: An absolute URI that is used to identify this activity definition when it is
        referenced in a specification, model, design or an instance; also called its
        canonical identifier. This SHOULD be globally unique and SHOULD be a literal
        address at which at which an authoritative instance of this activity
        definition is (or will be) published. This URL can be the target of a
        canonical reference. It SHALL remain the same when the activity definition is
        stored on different servers.
            :param identifier: A formal identifier that is used to identify this activity definition when it
        is represented in other formats, or referenced in a specification, model,
        design or an instance.
            :param version: The identifier that is used to identify this version of the activity
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the activity definition author
        and is not expected to be globally unique. For example, it might be a
        timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
        no expectation that versions can be placed in a lexicographical sequence. To
        provide a version consistent with the Decision Support Service specification,
        use the format Major.Minor.Revision (e.g. 1.0.0). For more information on
        versioning knowledge assets, refer to the Decision Support Service
        specification. Note that a version is required for non-experimental active
        assets.
            :param name: A natural language name identifying the activity definition. This name should
        be usable as an identifier for the module by machine processing applications
        such as code generation.
            :param title: A short, descriptive, user-friendly title for the activity definition.
            :param subtitle: An explanatory or alternate title for the activity definition giving
        additional information about its content.
            :param status: The status of this activity definition. Enables tracking the life-cycle of the
        content.
            :param experimental: A Boolean value to indicate that this activity definition is authored for
        testing purposes (or education/evaluation/marketing) and is not intended to be
        used for genuine usage.
            :param subjectCodeableConcept: None
            :param subjectReference: None
            :param date: The date  (and optionally time) when the activity definition was published.
        The date must change when the business version changes and it must change if
        the status code changes. In addition, it should change when the substantive
        content of the activity definition changes.
            :param publisher: The name of the organization or individual that published the activity
        definition.
            :param contact: Contact details to assist a user in finding and communicating with the
        publisher.
            :param description: A free text natural language description of the activity definition from a
        consumer's perspective.
            :param useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These contexts may be general categories (gender, age, ...)
        or may be references to specific programs (insurance plans, studies, ...) and
        may be used to assist with indexing and searching for appropriate activity
        definition instances.
            :param jurisdiction: A legal or geographic region in which the activity definition is intended to
        be used.
            :param purpose: Explanation of why this activity definition is needed and why it has been
        designed as it has.
            :param usage: A detailed description of how the activity definition is used from a clinical
        perspective.
            :param copyright: A copyright statement relating to the activity definition and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the activity definition.
            :param approvalDate: The date on which the resource content was approved by the publisher. Approval
        happens once when the content is officially approved for usage.
            :param lastReviewDate: The date on which the resource content was last reviewed. Review happens
        periodically after approval but does not change the original approval date.
            :param effectivePeriod: The period during which the activity definition content was or is planned to
        be in active use.
            :param topic: Descriptive topics related to the content of the activity. Topics provide a
        high-level categorization of the activity that can be useful for filtering and
        searching.
            :param author: An individiual or organization primarily involved in the creation and
        maintenance of the content.
            :param editor: An individual or organization primarily responsible for internal coherence of
        the content.
            :param reviewer: An individual or organization primarily responsible for review of some aspect
        of the content.
            :param endorser: An individual or organization responsible for officially endorsing the content
        for use in some setting.
            :param relatedArtifact: Related artifacts such as additional documentation, justification, or
        bibliographic references.
            :param library: A reference to a Library resource containing any formal logic used by the
        activity definition.
            :param kind: A description of the kind of resource the activity definition is representing.
        For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
        Typically, but not always, this is a Request resource.
            :param profile: A profile to which the target of the activity definition is expected to
        conform.
            :param code: Detailed description of the type of activity; e.g. What lab test, what
        procedure, what kind of encounter.
            :param intent: Indicates the level of authority/intentionality associated with the activity
        and where the request should fit into the workflow chain.
            :param priority: Indicates how quickly the activity  should be addressed with respect to other
        requests.
            :param doNotPerform: Set this to true if the definition is to indicate that a particular activity
        should NOT be performed. If true, this element should be interpreted to
        reinforce a negative coding. For example NPO as a code with a doNotPerform of
        true would still indicate to NOT perform the action.
            :param timingTiming: None
            :param timingDateTime: None
            :param timingAge: None
            :param timingPeriod: None
            :param timingRange: None
            :param timingDuration: None
            :param location: Identifies the facility where the activity will occur; e.g. home, hospital,
        specific clinic, etc.
            :param participant: Indicates who should participate in performing the action described.
            :param productReference: None
            :param productCodeableConcept: None
            :param quantity: Identifies the quantity expected to be consumed at once (per dose, per meal,
        etc.).
            :param dosage: Provides detailed dosage instructions in the same way that they are described
        for MedicationRequest resources.
            :param bodySite: Indicates the sites on the subject's body where the procedure should be
        performed (I.e. the target sites).
            :param specimenRequirement: Defines specimen requirements for the action to be performed, such as required
        specimens for a lab test.
            :param observationRequirement: Defines observation requirements for the action to be performed, such as body
        weight or surface area.
            :param observationResultRequirement: Defines the observations that are expected to be produced by the action.
            :param transform: A reference to a StructureMap resource that defines a transform that can be
        executed to produce the intent resource using the ActivityDefinition instance
        as the input.
            :param dynamicValue: Dynamic values that will be evaluated to produce values for elements of the
        resulting resource. For example, if the dosage of a medication must be
        computed based on the patient's weight, a dynamic value would be used to
        specify an expression that calculated the weight, and the path on the request
        resource that would contain the result.
        """
        super().__init__(
            resourceType="ActivityDefinition",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            subtitle=subtitle,
            status=status,
            experimental=experimental,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            usage=usage,
            copyright=copyright,
            approvalDate=approvalDate,
            lastReviewDate=lastReviewDate,
            effectivePeriod=effectivePeriod,
            topic=topic,
            author=author,
            editor=editor,
            reviewer=reviewer,
            endorser=endorser,
            relatedArtifact=relatedArtifact,
            library=library,
            kind=kind,
            profile=profile,
            code=code,
            intent=intent,
            priority=priority,
            doNotPerform=doNotPerform,
            timingTiming=timingTiming,
            timingDateTime=timingDateTime,
            timingAge=timingAge,
            timingPeriod=timingPeriod,
            timingRange=timingRange,
            timingDuration=timingDuration,
            location=location,
            participant=participant,
            productReference=productReference,
            productCodeableConcept=productCodeableConcept,
            quantity=quantity,
            dosage=dosage,
            bodySite=bodySite,
            specimenRequirement=specimenRequirement,
            observationRequirement=observationRequirement,
            observationResultRequirement=observationResultRequirement,
            transform=transform,
            dynamicValue=dynamicValue,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ActivityDefinitionSchema.get_schema(include_extension=include_extension)
