from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EventTimingCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-event-timing.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'EventTimingCode']) -> None:
            self.f: Callable[..., 'EventTimingCode'] = f

        def __get__(
            self, obj: Any, owner: Type['EventTimingCode']
        ) -> 'EventTimingCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'EventTimingCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EventTimingCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/event-timing
        """
        return "http://hl7.org/fhir/ValueSet/event-timing"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.75
        """
        return "2.16.840.1.113883.4.642.3.75"
