from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class LocationType(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-location-physical-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'LocationType']) -> None:
            self.f: Callable[..., 'LocationType'] = f

        def __get__(
            self, obj: Any, owner: Type['LocationType']
        ) -> 'LocationType':
            return self.f(owner)

    @classproperty
    def Site(cls) -> 'LocationType':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationType("si")

    @classproperty
    def Building(cls) -> 'LocationType':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationType("bu")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/location-physical-type
        """
        return "http://terminology.hl7.org/CodeSystem/location-physical-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.328
        """
        return "2.16.840.1.113883.4.642.3.328"
