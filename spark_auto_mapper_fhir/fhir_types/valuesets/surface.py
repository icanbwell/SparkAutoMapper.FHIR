from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirSurfaceCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-surface.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirSurfaceCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirSurfaceCode']) -> None:
            self.f: Callable[..., 'FhirSurfaceCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirSurfaceCode']
        ) -> 'FhirSurfaceCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirSurfaceCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirSurfaceCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/FDI-surface"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.546"
