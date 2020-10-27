from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.payment_adjustment_reason import PaymentAdjustmentReasonCode
from spark_auto_mapper_fhir.valuesets.payment_type import PaymentTypeCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.money import Money


class PaymentBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        type_: Optional[CodeableConcept[PaymentTypeCode]] = None,
        adjustment: Optional[Money] = None,
        adjustmentReason: Optional[CodeableConcept[PaymentAdjustmentReasonCode]
                                   ] = None,
        date: Optional[FhirDate] = None,
        amount: Optional[Money] = None,
        identifier: Optional[Identifier] = None
    ):
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
        super().__init__(
            type_=type_,
            adjustment=adjustment,
            adjustmentReason=adjustmentReason,
            date=date,
            amount=amount,
            identifier=identifier
        )
