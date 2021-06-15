from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class LocationTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-location-physical-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "LocationTypeCode"]) -> None:
            self.f: Callable[..., "LocationTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["LocationTypeCode"]
        ) -> "LocationTypeCode":
            return self.f(owner)

    @classproperty
    def Site(cls) -> "LocationTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("si")

    @classproperty
    def Building(cls) -> "LocationTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("bu")

    @classproperty
    def wing(cls) -> "LocationTypeCode":
        """
        A Wing within a Building, this often contains levels, rooms and corridors.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("wi")

    @classproperty
    def Ward(cls) -> "LocationTypeCode":
        """
        A Ward is a section of a medical facility that may contain rooms and other types of location.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("wa")

    @classproperty
    def level(cls) -> "LocationTypeCode":
        """
        A Level in a multi-level Building/Structure.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("lvl")

    @classproperty
    def Corridor(cls) -> "LocationTypeCode":
        """
        Any corridor within a Building, that may connect rooms.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("co")

    @classproperty
    def Room(cls) -> "LocationTypeCode":
        """
        A space that is allocated as a room, it may have walls/roof etc., but does not require these.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("ro")

    @classproperty
    def Bed(cls) -> "LocationTypeCode":
        """
        A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about, but the space it may occupy.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("bd")

    @classproperty
    def Vehicle(cls) -> "LocationTypeCode":
        """
        A means of transportation.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("ve")

    @classproperty
    def House(cls) -> "LocationTypeCode":
        """
        A residential dwelling. Usually used to reference a location that a person/patient may reside.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("ho")

    @classproperty
    def Cabinet(cls) -> "LocationTypeCode":
        """
        A container that can store goods, equipment, medications or other items.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("ca")

    @classproperty
    def Road(cls) -> "LocationTypeCode":
        """
        A defined path to travel between 2 points that has a known name.

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("rd")

    @classproperty
    def Area(cls) -> "LocationTypeCode":
        """
        A defined physical boundary of something, such as a flood risk zone, region, postcode

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("area")

    @classproperty
    def Jurisdiction(cls) -> "LocationTypeCode":
        """
        A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government - e.g. Ministry of Health), Province or State (community or Government), Business (throughout the enterprise), Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an physical boundary

        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("jdn")

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
