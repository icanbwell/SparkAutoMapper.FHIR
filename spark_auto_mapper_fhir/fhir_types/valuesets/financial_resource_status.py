from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirFinancialResourceStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-fm-status.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirFinancialResourceStatusCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirFinancialResourceStatusCode']
        ) -> None:
            self.f: Callable[..., 'FhirFinancialResourceStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirFinancialResourceStatusCode']
        ) -> 'FhirFinancialResourceStatusCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirFinancialResourceStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirFinancialResourceStatusCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/fm-status"
