from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class UnitsOfTimeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-units-of-time.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'UnitsOfTimeCode']) -> None:
            self.f: Callable[..., 'UnitsOfTimeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['UnitsOfTimeCode']
        ) -> 'UnitsOfTimeCode':
            return self.f(owner)

    @classproperty
    def second(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("s")

    @classproperty
    def minute(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("min")

    @classproperty
    def hour(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("h")

    @classproperty
    def day(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("d")

    @classproperty
    def week(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("wk")

    @classproperty
    def month(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("mo")

    @classproperty
    def year(cls) -> 'UnitsOfTimeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UnitsOfTimeCode("a")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/units-of-time
        """
        return "http://hl7.org/fhir/ValueSet/units-of-time"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.77
        """
        return "2.16.840.1.113883.4.642.3.77"
