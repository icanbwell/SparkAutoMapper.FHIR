from typing import Optional, Union
from pyspark.sql.types import StructType, DataType

from spark_auto_mapper_fhir.backbone_elements.goal_backbone_element import (
    GoalBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.date import FhirDate

from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext
from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.complex_types.identifier import Identifier

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri, FhirCanonical

from spark_fhir_schemas.r4.resources.plandefinition import PlanDefinitionSchema

from spark_auto_mapper_fhir.backbone_elements.action_backbone_element import (
    ActionBackboneElement,
)
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.resources.related_artifact import RelatedArtifact
from spark_auto_mapper_fhir.valuesets.definition_topic import DefinitionTopicCode
from spark_auto_mapper_fhir.valuesets.jurisdiction import JurisdictionCode
from spark_auto_mapper_fhir.valuesets.plan_definition_type import PlanDefinitionTypeCode
from spark_auto_mapper_fhir.valuesets.publication_status import PublicationStatusCode
from spark_auto_mapper_fhir.valuesets.subject_type import SubjectTypeCode


class PlanDefinition(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        status: PublicationStatusCode,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        type_: Optional[CodeableConcept[PlanDefinitionTypeCode]] = None,
        experimental: Optional[FhirBoolean] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[FhirList[CodeableConcept[JurisdictionCode]]] = None,
        purpose: Optional[FhirMarkdown] = None,
        usage: Optional[FhirString] = None,
        copyright_: Optional[FhirMarkdown] = None,
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
        goal: Optional[FhirList[GoalBackboneElement]] = None,
        action: Optional[FhirList[ActionBackboneElement]] = None,
    ) -> None:
        """
        PlanDefinition Resource in FHIR
        https://www.hl7.org/fhir/plandefinition.html
        The definition of a plan for a series of actions, independent of any specific patient or context
        + Warning: Name should be usable as an identifier for the module by machine processing applications
                    such as code generation


        :param id_: id of resource
        :param url: Canonical identifier for this plan definition, represented as a URI (globally unique)
        :param identifier: Additional identifier for the plan definition
        :param version: Business version of the plan definition
        :param name: Name for this plan definition (computer friendly)
        :param title: Name for this plan definition (human friendly)
        :param subtitle: Subordinate title of the plan definition
        :param type_: order-set | clinical-protocol | eca-rule | workflow-definition
        :param status: draft | active | retired | unknown
        :param experimental: For testing purposes, not real usage
        :param subjectCodeableConcept: Type of individual the plan definition is focused on
        :param subjectReference: Type of individual the plan definition is focused on
        :param date: Date last changed
        :param publisher: Name of the publisher (organization or individual)
        :param contact: Contact details for the publisher
        :param description: Natural language description of the plan definition
        :param useContext: The context that the content is intended to support
        :param jurisdiction: Intended jurisdiction for plan definition (if applicable)
        :param purpose: Why this plan definition is defined
        :param usage: Describes the clinical usage of the plan
        :param copyright_: 	Use and/or publishing restrictions
        :param approvalDate: When the plan definition was approved by publisher
        :param lastReviewDate: When the plan definition was last reviewed
        :param effectivePeriod: When the plan definition is expected to be used
        :param topic: E.g. Education, Treatment, Assessment
        :param author: Who authored the content
        :param editor: Who edited the content
        :param reviewer: Who reviewed the content
        :param endorser: Who endorsed the content
        :param relatedArtifact: Additional documentation, citations
        :param library: Logic used by the plan definition
        :param goal: What the plan is trying to accomplish
        :param action: Action defined by the plan
        """
        super().__init__(
            resourceType="PlanDefinition",
            id_=id_,
            meta=meta,
            extension=extension,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            subtitle=subtitle,
            type_=type_,
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
            copyright_=copyright_,
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
            goal=goal,
            action=action,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return PlanDefinitionSchema.get_schema(include_extension=include_extension)
