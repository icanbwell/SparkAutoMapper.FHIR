from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RequestPriorityCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-request-priority.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'RequestPriorityCode']) -> None:
            self.f: Callable[..., 'RequestPriorityCode'] = f

        def __get__(
            self, obj: Any, owner: Type['RequestPriorityCode']
        ) -> 'RequestPriorityCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'RequestPriorityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return RequestPriorityCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/request-priority"
