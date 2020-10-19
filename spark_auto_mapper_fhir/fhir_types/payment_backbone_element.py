from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.payment_adjustment_reason import FhirPaymentAdjustmentReasonCode
from spark_auto_mapper_fhir.fhir_types.valuesets.payment_type import FhirPaymentTypeCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney


class FhirPaymentBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        type_: Optional[FhirCodeableConcept[FhirPaymentTypeCode]] = None,
        adjustment: Optional[FhirMoney] = None,
        adjustmentReason: Optional[
            FhirCodeableConcept[FhirPaymentAdjustmentReasonCode]] = None,
        date: Optional[FhirDate] = None,
        amount: Optional[FhirMoney] = None,
        identifier: Optional[FhirIdentifier] = None
    ) -> 'FhirPaymentBackboneElement':
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
        return FhirPaymentBackboneElement(
            type_=type_,
            adjustment=adjustment,
            adjustmentReason=adjustmentReason,
            date=date,
            amount=amount,
            identifier=identifier
        )
