from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.backbone_elements.specific_cost_detail_backbone_element import \
    SpecificCostDetailBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class SpecificCostBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        category: CodeableConcept[FhirValueSetBase],
        benefit: Optional[FhirList[SpecificCostDetailBackboneElement]] = None
    ) -> None:
        """
        SpecificCostBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.plan.specificCost
        Specific costs


        :param category: General category of benefit
        :param benefit: Benefits list
        """
        super().__init__(category=category, benefit=benefit)
