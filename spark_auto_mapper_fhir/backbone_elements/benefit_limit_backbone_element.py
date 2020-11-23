from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.quantity import Quantity
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class BenefitLimitBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        value: Optional[Quantity] = None,
        code: Optional[CodeableConcept[FhirValueSetBase]] = None
    ) -> None:
        """
        BenefitLimitBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.coverage.benefit.limit
        Benefit limits


        :param value: Maximum value allowed
        :param code: Benefit limit details
        """
        super().__init__(id_=id_, extension=extension, value=value, code=code)
