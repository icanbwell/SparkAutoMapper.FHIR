from typing import Optional

from spark_auto_mapper_fhir.complex_types.expression import Expression
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase


class PlanDefinitionDynamicValueBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        path: Optional[FhirString] = None,
        expression: Optional[Expression] = None
    ) -> None:
        """
        PlanDefinitionDynamicValueBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.action.dynamicValue
        Dynamic aspects of the definition


        :param path: The path to the element to be set dynamically
        :param expression: 	An expression that provides the dynamic value for the customization
        """
        super().__init__(
            id_=id_, extension=extension, path=path, expression=expression
        )
