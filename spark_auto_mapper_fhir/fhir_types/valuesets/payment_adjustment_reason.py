from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirPaymentAdjustmentReasonCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-payment-adjustment-reason.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirPaymentAdjustmentReasonCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirPaymentAdjustmentReasonCode']
        ) -> None:
            self.f: Callable[..., 'FhirPaymentAdjustmentReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirPaymentAdjustmentReasonCode']
        ) -> 'FhirPaymentAdjustmentReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirPaymentAdjustmentReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirPaymentAdjustmentReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/payment-adjustment-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.600"
