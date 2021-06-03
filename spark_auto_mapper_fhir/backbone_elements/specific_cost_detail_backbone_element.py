from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.quantity import Quantity
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.benefit_cost_applicability import (
    BenefitCostApplicabilityCode,
)


class SpecificCostDetailBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: CodeableConcept[FhirValueSetBase],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        applicability: Optional[CodeableConcept[BenefitCostApplicabilityCode]] = None,
        qualifiers: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        value: Optional[Quantity] = None,
    ) -> None:
        """
        SpecificCostDetailBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.plan.specificCost.benefit.cost
        List of the costs


        :param type_: Type of cost
        :param applicability: in-network | out-of-network | other
        :param qualifiers: Additional information about the cost
        :param value: The actual cost value
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            applicability=applicability,
            qualifiers=qualifiers,
            value=value,
        )
