from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.backbone_elements.general_cost_backbone_element import (
    GeneralCostBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.specific_cost_backbone_element import (
    SpecificCostBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class InsurancePlanBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        type_: Optional[CodeableConcept[FhirValueSetBase]] = None,
        coverageArea: Optional[FhirList[Reference[Location]]] = None,
        network: Optional[FhirList[Reference[Organization]]] = None,
        generalCost: Optional[FhirList[GeneralCostBackboneElement]] = None,
        specificCost: Optional[FhirList[SpecificCostBackboneElement]] = None,
    ) -> None:
        """
        InsurancePlanBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.plan
        Plan details


        :param identifier: Business Identifier for Product
        :param type_: Type of plan
        :param coverageArea: Where product applies
        :param network: What networks provide coverage
        :param generalCost: Overall costs
        :param specificCost: Specific costs
        """
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            type_=type_,
            coverageArea=coverageArea,
            network=network,
            generalCost=generalCost,
            specificCost=specificCost,
        )
