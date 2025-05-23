from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # actionId (id)
    # relationship (ActionRelationshipType)
    from spark_auto_mapper_fhir.value_sets.action_relationship_type import (
        ActionRelationshipTypeCode,
    )

    # offsetDuration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # offsetRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PlanDefinitionRelatedAction(FhirBackboneElementBase):
    """
    PlanDefinition.RelatedAction
        This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        actionId: FhirId,
        relationship: ActionRelationshipTypeCode,
        offsetDuration: Optional[Duration] = None,
        offsetRange: Optional[Range] = None,
    ) -> None:
        """
            This resource allows for the definition of various types of plans as a
        sharable, consumable, and executable artifact. The resource is general enough
        to support the description of a broad range of clinical artifacts such as
        clinical decision support rules, order sets and protocols.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param actionId: The element id of the related action.
            :param relationship: The relationship of this action to the related action.
            :param offsetDuration: None
            :param offsetRange: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            actionId=actionId,
            relationship=relationship,
            offsetDuration=offsetDuration,
            offsetRange=offsetRange,
        )
