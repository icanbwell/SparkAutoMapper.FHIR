from typing import Optional

from spark_auto_mapper_fhir.complex_types.duration import Duration

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.observation_code import LOINCCode


class TargetBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        measure: Optional[CodeableConcept[LOINCCode]] = None,
        detailQuantity: Optional[Quantity] = None,
        detailRange: Optional[Range] = None,
        detailCodeableConcept: Optional[CodeableConcept[FhirValueSetBase]] = None,
        due: Optional[Duration] = None,
    ) -> None:
        """
        TargetBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.goal.target
        Target outcome for the goal


        :param measure: The parameter whose value is to be tracked
        :param detailQuantity: The target value to be achieved
        :param detailRange: The target value to be achieved
        :param detailCodeableConcept: The target value to be achieved
        :param due: Reach goal within
        """
        super().__init__(
            id_=id_,
            extension=extension,
            measure=measure,
            detailQuantity=detailQuantity,
            detailRange=detailRange,
            detailCodeableConcept=detailCodeableConcept,
            due=due,
        )
