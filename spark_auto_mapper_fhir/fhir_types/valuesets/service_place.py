from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirServicePlaceCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-service-place.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirServicePlaceCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirServicePlaceCode']) -> None:
            self.f: Callable[..., 'FhirServicePlaceCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirServicePlaceCode']
        ) -> 'FhirServicePlaceCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirServicePlaceCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirServicePlaceCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-serviceplace"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.564"
