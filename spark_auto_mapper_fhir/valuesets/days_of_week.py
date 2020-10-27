from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DaysOfWeek(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-days-of-week.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'DaysOfWeek']) -> None:
            self.f: Callable[..., 'DaysOfWeek'] = f

        def __get__(self, obj: Any, owner: Type['DaysOfWeek']) -> 'DaysOfWeek':
            return self.f(owner)

    @classproperty
    def Monday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("mon")

    @classproperty
    def Tuesday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("tue")

    @classproperty
    def Wednesday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("wed")

    @classproperty
    def Thursday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("thu")

    @classproperty
    def Friday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("fri")

    @classproperty
    def Saturday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("sat")

    @classproperty
    def Sunday(cls) -> 'DaysOfWeek':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DaysOfWeek("sun")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/days-of-week"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.512"
