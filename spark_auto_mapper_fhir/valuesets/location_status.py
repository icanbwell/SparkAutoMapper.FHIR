from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class LocationStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-location-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "LocationStatusCode"]) -> None:
            self.f: Callable[..., "LocationStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["LocationStatusCode"]
        ) -> "LocationStatusCode":
            return self.f(owner)

    @classproperty
    def Active(cls) -> "LocationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationStatusCode("active")

    @classproperty
    def Suspended(cls) -> "LocationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationStatusCode("suspended")

    @classproperty
    def Inactive(cls) -> "LocationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationStatusCode("inactive")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/location-status
        """
        return "http://hl7.org/fhir/location-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.332
        """
        return "2.16.840.1.113883.4.642.3.332"
