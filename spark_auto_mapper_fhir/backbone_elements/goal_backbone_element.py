from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.backbone_elements.target_backbone_element import (
    TargetBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.related_artifact import RelatedArtifact
from spark_auto_mapper_fhir.valuesets.condition import ConditionCode
from spark_auto_mapper_fhir.valuesets.goal_category import GoalCategoryCode
from spark_auto_mapper_fhir.valuesets.goal_priority import GoalPriorityCode
from spark_auto_mapper_fhir.valuesets.goal_start_event import GoalStartEventCode
from spark_auto_mapper_fhir.valuesets.snomed_clinical_finding import (
    SNOMEDCTClinicalFindingsCode,
)


class GoalBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        description: CodeableConcept[SNOMEDCTClinicalFindingsCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        category: Optional[CodeableConcept[GoalCategoryCode]] = None,
        priority: Optional[CodeableConcept[GoalPriorityCode]] = None,
        start: Optional[CodeableConcept[GoalStartEventCode]] = None,
        addresses: Optional[FhirList[CodeableConcept[ConditionCode]]] = None,
        documentation: Optional[FhirList[RelatedArtifact]] = None,
        target: Optional[FhirList[TargetBackboneElement]] = None,
    ) -> None:
        """
        GoalBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition.html#PlanDefinition.action
        What the plan is trying to accomplish


        :param category: E.g. Treatment, dietary, behavioral
        :param description: Code or text describing the goal
        :param priority: high-priority | medium-priority | low-priority
        :param start: When goal pursuit begins
        :param addresses: What does the goal address
        :param documentation: Supporting documentation for the goal
        :param target: Target outcome for the goal
        """
        super().__init__(
            id_=id_,
            extension=extension,
            category=category,
            description=description,
            priority=priority,
            start=start,
            addresses=addresses,
            documentation=documentation,
            target=target,
        )
