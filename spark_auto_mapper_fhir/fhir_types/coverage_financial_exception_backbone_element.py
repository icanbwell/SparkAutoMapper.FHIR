from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.coverage_financial_exception import FhirCoverageFinancialExceptionCode
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod


class FhirCoverageFinancialExceptionBackboneElement(FhirResourceBase):
    @classmethod
    def map(
        cls,
        type_: FhirCodeableConcept[FhirCoverageFinancialExceptionCode],
        period: Optional[FhirPeriod] = None
    ) -> 'FhirCoverageFinancialExceptionBackboneElement':
        """
        CoverageFinancialExceptionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.costToBeneficiary.exception
        Exceptions for patient payments

        :param type_: Exception category. https://hl7.org/FHIR/valueset-coverage-financial-exception.html
        :param period: The effective period of the exception
        """
        return FhirCoverageFinancialExceptionBackboneElement(
            type_=type_, period=period
        )
