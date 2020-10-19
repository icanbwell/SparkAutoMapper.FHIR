from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SurfaceCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-surface.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'SurfaceCode']) -> None:
            self.f: Callable[..., 'SurfaceCode'] = f

        def __get__(
            self, obj: Any, owner: Type['SurfaceCode']
        ) -> 'SurfaceCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'SurfaceCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SurfaceCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/FDI-surface"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.546"
