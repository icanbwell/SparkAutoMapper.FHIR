from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class TriggerTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-trigger-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "TriggerTypeCode"]) -> None:
            self.f: Callable[..., "TriggerTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["TriggerTypeCode"]
        ) -> "TriggerTypeCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("A")

    @classproperty
    def named_event(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("named-event")

    @classproperty
    def periodic(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("periodic")

    @classproperty
    def data_changed(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-changed")

    @classproperty
    def data_added(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-added")

    @classproperty
    def data_modified(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-modified")

    @classproperty
    def data_removed(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-removed")

    @classproperty
    def data_accessed(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-accessed")

    @classproperty
    def data_access_ended(cls) -> "TriggerTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TriggerTypeCode("data-access-ended")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/trigger-type
        """
        return "http://hl7.org/fhir/ValueSet/trigger-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.103
        """
        return "2.16.840.1.113883.4.642.3.103"
