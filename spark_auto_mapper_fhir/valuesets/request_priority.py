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
    def Routine(cls) -> 'RequestPriorityCode':
        """
        The request has normal priority.
        """
        # noinspection PyCallingNonCallable
        return RequestPriorityCode("routine")

    @classproperty
    def Urgent(cls) -> 'RequestPriorityCode':
        """
        The request should be actioned promptly - higher priority than routine.
        """
        # noinspection PyCallingNonCallable
        return RequestPriorityCode("urgent")

    @classproperty
    def ASAP(cls) -> 'RequestPriorityCode':
        """
        The request should be actioned as soon as possible - higher priority than urgent.
        """
        # noinspection PyCallingNonCallable
        return RequestPriorityCode("asap")

    @classproperty
    def STAT(cls) -> 'RequestPriorityCode':
        """
        The request should be actioned immediately - highest possible priority. E.g. an emergency.
        """
        # noinspection PyCallingNonCallable
        return RequestPriorityCode("stat")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/request-priority"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.115
        """
        return "2.16.840.1.113883.4.642.3.115"
