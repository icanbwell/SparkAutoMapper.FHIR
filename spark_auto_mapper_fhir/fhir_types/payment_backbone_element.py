from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier
from spark_auto_mapper_fhir.fhir_types.money import AutoMapperFhirDataTypeMoney


class AutoMapperFhirDataTypePaymentBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            adjustment: Optional[AutoMapperFhirDataTypeMoney] = None,
            adjustmentReason: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            date: Optional[AutoMapperDateInputType] = None,
            amount: Optional[AutoMapperFhirDataTypeMoney] = None,
            identifier: Optional[AutoMapperFhirDataTypeIdentifier] = None
            ) -> 'AutoMapperFhirDataTypePaymentBackboneElement':
        """
        PaymentBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit.html
        Payment Details

        :param type_: Partial or complete payment. https://hl7.org/FHIR/valueset-ex-paymenttype.html
        :param adjustment: Payment adjustment for non-claim issues
        :param adjustmentReason: Explanation for the variance. https://hl7.org/FHIR/valueset-payment-adjustment-reason.html
        :param date: Expected date of payment
        :param amount: Payable amount after adjustment
        :param identifier: Business identifier for the payment
        """
        return AutoMapperFhirDataTypePaymentBackboneElement(
            type_=type_,
            adjustment=adjustment,
            adjustmentReason=adjustmentReason,
            date=date,
            amount=amount,
            identifier=identifier
        )
