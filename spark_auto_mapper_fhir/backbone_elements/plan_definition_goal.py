from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact
    from spark_auto_mapper_fhir.backbone_elements.plan_definition_target import (
        PlanDefinitionTarget,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PlanDefinitionGoal(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        category: Optional[CodeableConcept] = None,
        description: CodeableConcept,
        priority: Optional[CodeableConcept] = None,
        start: Optional[CodeableConcept] = None,
        addresses: Optional[FhirList[CodeableConcept]] = None,
        documentation: Optional[FhirList[RelatedArtifact]] = None,
        target: Optional[FhirList[PlanDefinitionTarget]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param category: Indicates a category the goal falls within.
            :param description: Human-readable and/or coded description of a specific desired objective of
        care, such as "control blood pressure" or "negotiate an obstacle course" or
        "dance with child at wedding".
            :param priority: Identifies the expected level of importance associated with
        reaching/sustaining the defined goal.
            :param start: The event after which the goal should begin being pursued.
            :param addresses: Identifies problems, conditions, issues, or concerns the goal is intended to
        address.
            :param documentation: Didactic or other informational resources associated with the goal that
        provide further supporting information about the goal. Information resources
        can include inline text commentary and links to web resources.
            :param target: Indicates what should be done and within what timeframe.
        """
        super().__init__(
            resourceType="PlanDefinitionGoal",
            id_=id_,
            meta=meta,
            extension=extension,
            category=category,
            description=description,
            priority=priority,
            start=start,
            addresses=addresses,
            documentation=documentation,
            target=target,
        )