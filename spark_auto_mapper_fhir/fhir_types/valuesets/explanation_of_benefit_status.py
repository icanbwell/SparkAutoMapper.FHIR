from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirExplanationOfBenefitStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-explanationofbenefit-status.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirExplanationOfBenefitStatusCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirExplanationOfBenefitStatusCode']
        ) -> None:
            self.f: Callable[..., 'FhirExplanationOfBenefitStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirExplanationOfBenefitStatusCode']
        ) -> 'FhirExplanationOfBenefitStatusCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirExplanationOfBenefitStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirExplanationOfBenefitStatusCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/explanationofbenefit-status"
