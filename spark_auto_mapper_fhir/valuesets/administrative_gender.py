from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class AdministrativeGenderCode(FhirValueSetBase):
    def __init__(self, value: AutoMapperTextInputType):
        assert not isinstance(value, str) or value in [
            "male",
            "female",
            "other",
            "unknown",
        ]
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AdministrativeGenderCode"]) -> None:
            self.f: Callable[..., "AdministrativeGenderCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AdministrativeGenderCode"]
        ) -> "AdministrativeGenderCode":
            return self.f(owner)

    # noinspection PyMethodParameters
    @classproperty
    def male(cls) -> "AdministrativeGenderCode":
        """
        Male
        """
        # noinspection PyCallingNonCallable
        return AdministrativeGenderCode("male")

    # noinspection PyMethodParameters
    @classproperty
    def female(cls) -> "AdministrativeGenderCode":
        """
        Female
        """
        # noinspection PyCallingNonCallable
        return AdministrativeGenderCode("female")

    # noinspection PyMethodParameters
    @classproperty
    def other(cls) -> "AdministrativeGenderCode":
        """
        Other
        """
        # noinspection PyCallingNonCallable
        return AdministrativeGenderCode("other")

    # noinspection PyMethodParameters
    @classproperty
    def unknown(cls) -> "AdministrativeGenderCode":
        """
        Unknown
        """
        # noinspection PyCallingNonCallable
        return AdministrativeGenderCode("unknown")
