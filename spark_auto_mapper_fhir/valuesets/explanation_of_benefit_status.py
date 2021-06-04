from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ExplanationOfBenefitStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-explanationofbenefit-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ExplanationOfBenefitStatusCode"]) -> None:
            self.f: Callable[..., "ExplanationOfBenefitStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ExplanationOfBenefitStatusCode"]
        ) -> "ExplanationOfBenefitStatusCode":
            return self.f(owner)

    @classproperty
    def Active(cls) -> "ExplanationOfBenefitStatusCode":
        """
        The resource instance is curently in-force.
        """
        # noinspection PyCallingNonCallable
        return ExplanationOfBenefitStatusCode("active")

    def Cancelled(cls) -> "ExplanationOfBenefitStatusCode":
        """
        The resource instance is withdrawn, rescinded or reversed.
        """
        # noinspection PyCallingNonCallable
        return ExplanationOfBenefitStatusCode("cancelled")

    def Draft(cls) -> "ExplanationOfBenefitStatusCode":
        """
        A new resource instance the contents of which is not complete
        """
        # noinspection PyCallingNonCallable
        return ExplanationOfBenefitStatusCode("draft")

    def EnteredInError(cls) -> "ExplanationOfBenefitStatusCode":
        """
        The resource instance was entered in error.
        """
        # noinspection PyCallingNonCallable
        return ExplanationOfBenefitStatusCode("entered-in-error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/explanationofbenefit-status"
