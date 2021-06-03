from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.backbone_elements.specific_cost_detail_backbone_element import (
    SpecificCostDetailBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class SpecificCostBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        category: CodeableConcept[FhirValueSetBase],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        benefit: Optional[FhirList[SpecificCostDetailBackboneElement]] = None,
    ) -> None:
        """
        SpecificCostBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.plan.specificCost
        Specific costs


        :param category: General category of benefit
        :param benefit: Benefits list
        """
        super().__init__(
            id_=id_, extension=extension, category=category, benefit=benefit
        )
