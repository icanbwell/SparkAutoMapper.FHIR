from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SlotStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-slotstatus.html
    busy | free | busy-unavailable | busy-tentative | entered-in-error
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'SlotStatusCode']) -> None:
            self.f: Callable[..., 'SlotStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['SlotStatusCode']
        ) -> 'SlotStatusCode':
            return self.f(owner)

    @classproperty
    def Busy(cls) -> 'SlotStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SlotStatusCode("busy")

    @classproperty
    def Free(cls) -> 'SlotStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SlotStatusCode("free")

    @classproperty
    def BusyUnavailable(cls) -> 'SlotStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SlotStatusCode("busy-unavailable")

    @classproperty
    def BusyTentative(cls) -> 'SlotStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SlotStatusCode("busy-tentative")

    @classproperty
    def EnteredInError(cls) -> 'SlotStatusCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SlotStatusCode("entered-in-error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/slotstatus
        """
        return "http://hl7.org/fhir/slotstatus"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.4.483
        """
        return "2.16.840.1.113883.4.642.4.483"
