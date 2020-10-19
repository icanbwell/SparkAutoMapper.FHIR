from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirProcessPriorityCode(FhirValueSetBase):
    """
    https://terminology.hl7.org/1.0.0/CodeSystem-processpriority.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirProcessPriorityCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirProcessPriorityCode']
        ) -> None:
            self.f: Callable[..., 'FhirProcessPriorityCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirProcessPriorityCode']
        ) -> 'FhirProcessPriorityCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirProcessPriorityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirProcessPriorityCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/processpriority"
