from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirToothCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-tooth.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirToothCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirToothCode']) -> None:
            self.f: Callable[..., 'FhirToothCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirToothCode']
        ) -> 'FhirToothCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirToothCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirToothCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-tooth"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.540"
