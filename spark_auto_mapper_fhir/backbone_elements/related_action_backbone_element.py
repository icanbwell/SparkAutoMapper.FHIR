from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.action_relationship_type import (
    ActionRelationshipTypeCode,
)
from spark_auto_mapper_fhir.complex_types.duration import Duration
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)


# noinspection PyPep8Naming
class RelatedActionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        actionId: FhirId,
        relationship: ActionRelationshipTypeCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        offsetDuration: Optional[Duration] = None,
        offsetRange: Optional[Range] = None,
    ) -> None:
        """
        RelatedActionBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.action.relatedAction
        Relationship to another action


        :param actionId: What action is this related to
        :param relationship: before-start | before | before-end | concurrent-with-start | concurrent
                                | concurrent-with-end | after-start | after | after-end
        :param offsetDuration: Time offset for the relationship
        :param offsetRange: Time offset for the relationship
        """
        super().__init__(
            id_=id_,
            extension=extension,
            actionId=actionId,
            relationship=relationship,
            offsetDuration=offsetDuration,
            offsetRange=offsetRange,
        )
