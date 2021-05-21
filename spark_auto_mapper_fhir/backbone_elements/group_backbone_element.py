from typing import Optional, Any

from spark_auto_mapper_fhir.backbone_elements.population_backbone_element import PopulationBackboneElement
from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase


class GroupBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        code: Optional[CodeableConcept[Any]] = None,
        population: Optional[FhirList[PopulationBackboneElement]] = None,
        measureScore: Optional[Quantity] = None,
        # stratifier: Optional[FhirList[StratifierBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        super().__init__(
            id_=id_,
            code=code,
            population=population,
            measureScore=measureScore,
            # stratifier=stratifier,
            extension=extension,
        )
