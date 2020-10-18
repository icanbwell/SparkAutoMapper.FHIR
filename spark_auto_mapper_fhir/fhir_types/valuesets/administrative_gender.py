from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType


class FhirAdministrativeGenderCode(AutoMapperDataTypeLiteral):
    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirAdministrativeGenderCode':
        assert value in ["male", "female", "other", "unknown"]
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirAdministrativeGenderCode']) -> None:
            self.f: Callable[..., 'FhirAdministrativeGenderCode'] = f

        def __get__(self, obj: Any, owner: Type['FhirAdministrativeGenderCode']) -> 'FhirAdministrativeGenderCode':
            return self.f(owner)

    # noinspection PyMethodParameters
    @classproperty
    def male(cls) -> 'FhirAdministrativeGenderCode':
        """
        Male
        """
        # noinspection PyCallingNonCallable
        return FhirAdministrativeGenderCode("male")

    # noinspection PyMethodParameters
    @classproperty
    def female(cls) -> 'FhirAdministrativeGenderCode':
        """
        Female
        """
        # noinspection PyCallingNonCallable
        return FhirAdministrativeGenderCode("female")

    # noinspection PyMethodParameters
    @classproperty
    def other(cls) -> 'FhirAdministrativeGenderCode':
        """
        Other
        """
        # noinspection PyCallingNonCallable
        return FhirAdministrativeGenderCode("other")

    # noinspection PyMethodParameters
    @classproperty
    def unknown(cls) -> 'FhirAdministrativeGenderCode':
        """
        Unknown
        """
        # noinspection PyCallingNonCallable
        return FhirAdministrativeGenderCode("unknown")
