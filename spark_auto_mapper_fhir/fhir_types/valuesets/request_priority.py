from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirRequestPriorityCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-request-priority.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirRequestPriorityCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirRequestPriorityCode']
        ) -> None:
            self.f: Callable[..., 'FhirRequestPriorityCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirRequestPriorityCode']
        ) -> 'FhirRequestPriorityCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirRequestPriorityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirRequestPriorityCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/request-priority"
