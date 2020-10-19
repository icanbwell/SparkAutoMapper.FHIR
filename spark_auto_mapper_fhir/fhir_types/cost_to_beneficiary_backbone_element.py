from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.coverage_copay_type import FhirCoverageCopayTypeCode
from spark_auto_mapper_fhir.fhir_types.coverage_financial_exception_backbone_element import \
    FhirCoverageFinancialExceptionBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney
from spark_auto_mapper_fhir.fhir_types.simple_quantity import FhirSimpleQuantity


class FhirCostToBeneficiaryBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        type_: Optional[FhirCodeableConcept[FhirCoverageCopayTypeCode]] = None,
        valueQuantity: Optional[FhirSimpleQuantity] = None,
        valueMoney: Optional[FhirMoney] = None,
        exception: Optional[
            FhirList[FhirCoverageFinancialExceptionBackboneElement]] = None
    ) -> 'FhirCostToBeneficiaryBackboneElement':
        """
        CostToBeneficiaryBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.costToBeneficiary
        Patient payments for services/products

        :param type_: Cost category. https://hl7.org/FHIR/valueset-coverage-copay-type.html
        :param valueQuantity: The amount or percentage due from the beneficiary
        :param valueMoney: 	The amount or percentage due from the beneficiary
        :param exception: Exceptions for patient payments
        """
        return FhirCostToBeneficiaryBackboneElement(
            type_=type_,
            valueQuantity=valueQuantity,
            valueMoney=valueMoney,
            exception=exception
        )
