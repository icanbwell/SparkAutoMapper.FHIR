from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimPayeeTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-payeetype.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimPayeeTypeCode"]) -> None:
            self.f: Callable[..., "ClaimPayeeTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ClaimPayeeTypeCode"]
        ) -> "ClaimPayeeTypeCode":
            return self.f(owner)

    @classproperty
    def Subscriber(cls) -> "ClaimPayeeTypeCode":
        """
        The subscriber (policy holder) will be reimbursed.
        """
        # noinspection PyCallingNonCallable
        return ClaimPayeeTypeCode("subscriber")

    def Provider(cls) -> "ClaimPayeeTypeCode":
        """
        Any benefit payable will be paid to the provider (Assignment of Benefit).
        """
        # noinspection PyCallingNonCallable
        return ClaimPayeeTypeCode("provider")

    def Other(cls) -> "ClaimPayeeTypeCode":
        """
        Any benefit payable will be paid to a third party such as a guarrantor.
        """
        # noinspection PyCallingNonCallable
        return ClaimPayeeTypeCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/payeetype"
