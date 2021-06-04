from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CoverageFinancialExceptionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-coverage-financial-exception.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "CoverageFinancialExceptionCode"]) -> None:
            self.f: Callable[..., "CoverageFinancialExceptionCode"] = f

        def __get__(
            self, obj: Any, owner: Type["CoverageFinancialExceptionCode"]
        ) -> "CoverageFinancialExceptionCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "CoverageFinancialExceptionCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CoverageFinancialExceptionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception"
