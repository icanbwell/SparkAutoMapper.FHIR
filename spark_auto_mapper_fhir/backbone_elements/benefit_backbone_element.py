from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.benefit_limit_backbone_element import (
    BenefitLimitBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class BenefitBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: CodeableConcept[FhirValueSetBase],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        requirement: Optional[FhirString] = None,
        limit: Optional[FhirList[BenefitLimitBackboneElement]] = None,
    ) -> None:
        """
        BenefitBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.coverage.benefit
        List of benefits


        :param type_: Type of benefit
        :param requirement: Referral requirements
        :param limit: Benefit limits
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            requirement=requirement,
            limit=limit,
        )
