from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.benefit_backbone_element import (
    BenefitBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class InsurancePlanCoverageBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: CodeableConcept[FhirValueSetBase],
        benefit: FhirList[BenefitBackboneElement],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        network: Optional[FhirList[Reference[Organization]]] = None,
    ) -> None:
        """
        InsurancePlanCoverageBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.coverage
        Coverage details


        :param type_: Type of coverage
        :param benefit: List of benefits
        :param network: What networks provide coverage
        """
        super().__init__(
            id_=id_, extension=extension, type_=type_, benefit=benefit, network=network
        )
