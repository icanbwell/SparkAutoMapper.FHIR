from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.coverage_copay_type import CoverageCopayTypeCode
from spark_auto_mapper_fhir.backbone_elements.coverage_financial_exception_backbone_element import \
    CoverageFinancialExceptionBackboneElement
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity


class CostToBeneficiaryBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        type_: Optional[CodeableConcept[CoverageCopayTypeCode]] = None,
        valueQuantity: Optional[SimpleQuantity] = None,
        valueMoney: Optional[Money] = None,
        exception: Optional[FhirList[CoverageFinancialExceptionBackboneElement]
                            ] = None
    ):
        """
        CostToBeneficiaryBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.costToBeneficiary
        Patient payments for services/products

        :param type_: Cost category. https://hl7.org/FHIR/valueset-coverage-copay-type.html
        :param valueQuantity: The amount or percentage due from the beneficiary
        :param valueMoney: 	The amount or percentage due from the beneficiary
        :param exception: Exceptions for patient payments
        """
        super().__init__(
            type_=type_,
            valueQuantity=valueQuantity,
            valueMoney=valueMoney,
            exception=exception
        )
