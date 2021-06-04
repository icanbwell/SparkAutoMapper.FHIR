from typing import Optional

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase

from spark_auto_mapper_fhir.backbone_elements.population_backbone_element import (
    PopulationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.stratifier_backbone_element import (
    StratifierBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)


class GroupBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        code: Optional[CodeableConcept[FhirValueSetBase]] = None,
        population: Optional[FhirList[PopulationBackboneElement]] = None,
        measureScore: Optional[Quantity] = None,
        stratifier: Optional[FhirList[StratifierBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        GroupBackboneElement Resource in FHIR
        https://www.hl7.org/fhir/measurereport.html#MeasureReport.group


        :param code: Meaning of the group
        :param population: The populations in the group
        :param measureScore: What score this group achieved
        :param stratifier: Stratification results
        """
        super().__init__(
            id_=id_,
            code=code,
            population=population,
            measureScore=measureScore,
            stratifier=stratifier,
            extension=extension,
        )
