from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class PaymentAdjustmentReasonCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-payment-adjustment-reason.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'PaymentAdjustmentReasonCode']
        ) -> None:
            self.f: Callable[..., 'PaymentAdjustmentReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['PaymentAdjustmentReasonCode']
        ) -> 'PaymentAdjustmentReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'PaymentAdjustmentReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PaymentAdjustmentReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/payment-adjustment-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.600"
