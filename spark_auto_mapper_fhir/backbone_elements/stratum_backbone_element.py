from typing import Optional

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.backbone_elements.population_backbone_element import (
    PopulationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.stratum_component_backbone_element import (
    StratumComponentBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class StratumBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        value: Optional[CodeableConcept[FhirValueSetBase]] = None,
        component: Optional[FhirList[StratumComponentBackboneElement]] = None,
        population: Optional[FhirList[PopulationBackboneElement]] = None,
        measureScore: Optional[Quantity] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        StratumBackboneElement Resource in FHIR
        https://www.hl7.org/fhir/measurereport.html#MeasureReport.stratifier.stratum


        :param value: The stratum value, e.g. male
        :param component: Stratifier component values
        :param population: Population results in the stratum
        :param measureScore: What score this stratum achieved
        """
        super().__init__(
            id_=id_,
            value=value,
            component=component,
            population=population,
            measureScore=measureScore,
            extension=extension,
        )
