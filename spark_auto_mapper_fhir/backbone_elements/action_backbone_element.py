from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.condition_backbone_element import ConditionBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.trigger_definition import TriggerDefinition
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class ActionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        code: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        trigger: Optional[FhirList[TriggerDefinition]] = None,
        condition: Optional[FhirList[ConditionBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        ActionBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.action
        """
        super().__init__(
            id_=id_,
            code=code,
            trigger=trigger,
            condition=condition,
            extension=extension
        )
