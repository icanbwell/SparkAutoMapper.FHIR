from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RemittanceOutcomeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-remittance-outcome.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "RemittanceOutcomeCode"]) -> None:
            self.f: Callable[..., "RemittanceOutcomeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["RemittanceOutcomeCode"]
        ) -> "RemittanceOutcomeCode":
            return self.f(owner)

    @classproperty
    def Queued(cls) -> "RemittanceOutcomeCode":
        """
        The Claim/Pre-authorization/Pre-determination has been received but processing has not begun.
        """
        # noinspection PyCallingNonCallable
        return RemittanceOutcomeCode("queued")

    def ProcessingComplete(cls) -> "RemittanceOutcomeCode":
        """
        The processing has completed without errors
        """
        # noinspection PyCallingNonCallable
        return RemittanceOutcomeCode("complete")

    def Error(cls) -> "RemittanceOutcomeCode":
        """
        One or more errors have been detected in the Claim
        """
        # noinspection PyCallingNonCallable
        return RemittanceOutcomeCode("error")

    def PartialProcessing(cls) -> "RemittanceOutcomeCode":
        """
        No errors have been detected in the Claim and some of the adjudication has been performed.
        """
        # noinspection PyCallingNonCallable
        return RemittanceOutcomeCode("partial")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/remittance-outcome"
