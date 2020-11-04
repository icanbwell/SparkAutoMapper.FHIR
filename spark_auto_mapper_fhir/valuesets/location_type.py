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
        def __init__(self, f: Callable[..., 'LocationTypeCode']) -> None:
            self.f: Callable[..., 'LocationTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['LocationTypeCode']
        ) -> 'LocationTypeCode':
            return self.f(owner)

    @classproperty
    def Site(cls) -> 'LocationTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("si")

    @classproperty
    def Building(cls) -> 'LocationTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return LocationTypeCode("bu")

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
