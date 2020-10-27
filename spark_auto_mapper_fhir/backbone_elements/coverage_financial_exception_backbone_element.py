from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.coverage_financial_exception import CoverageFinancialExceptionCode
from spark_auto_mapper_fhir.complex_types.period import Period


class CoverageFinancialExceptionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: CodeableConcept[CoverageFinancialExceptionCode],
        period: Optional[Period] = None
    ):
        """
        CoverageFinancialExceptionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.costToBeneficiary.exception
        Exceptions for patient payments

        :param type_: Exception category. https://hl7.org/FHIR/valueset-coverage-financial-exception.html
        :param period: The effective period of the exception
        """
        super().__init__(type_=type_, period=period)
