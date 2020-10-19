from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirConditionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-condition-code.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirConditionCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirConditionCode']) -> None:
            self.f: Callable[..., 'FhirConditionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirConditionCode']
        ) -> 'FhirConditionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirConditionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirConditionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://snomed.info/sct"
