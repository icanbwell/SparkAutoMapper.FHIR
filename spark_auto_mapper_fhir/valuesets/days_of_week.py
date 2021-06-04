from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DaysOfWeekCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-days-of-week.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "DaysOfWeekCode"]) -> None:
            self.f: Callable[..., "DaysOfWeekCode"] = f

        def __get__(self, obj: Any, owner: Type["DaysOfWeekCode"]) -> "DaysOfWeekCode":
            return self.f(owner)

    @classproperty
    def Monday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("mon")

    @classproperty
    def Tuesday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("tue")

    @classproperty
    def Wednesday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("wed")

    @classproperty
    def Thursday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("thu")

    @classproperty
    def Friday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("fri")

    @classproperty
    def Saturday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("sat")

    @classproperty
    def Sunday(cls) -> "DaysOfWeekCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeekCode("sun")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/days-of-week"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.512"
