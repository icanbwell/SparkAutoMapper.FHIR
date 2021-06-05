from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class LocationModeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-location-mode.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "LocationModeCode"]) -> None:
            self.f: Callable[..., "LocationModeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["LocationModeCode"]
        ) -> "LocationModeCode":
            return self.f(owner)

    @classproperty
    def Instance(cls) -> "LocationModeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationModeCode("instance")

    @classproperty
    def Kind(cls) -> "LocationModeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationModeCode("kind")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/location-mode
        """
        return "http://hl7.org/fhir/location-mode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.330
        """
        return "2.16.840.1.113883.4.642.3.330"
