from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EventStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://www.hl7.org/fhir/valueset-event-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EventStatusCode"]) -> None:
            self.f: Callable[..., "EventStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EventStatusCode"]
        ) -> "EventStatusCode":
            return self.f(owner)

    @classproperty
    def preparation(cls) -> "EventStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EventStatusCode("preparation")

    @classproperty
    def InProgress(cls) -> "EventStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EventStatusCode("in-progress")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/event-status
        """
        return "http://hl7.org/fhir/ValueSet/event-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.109
        """
        return "2.16.840.1.113883.4.642.3.109"
