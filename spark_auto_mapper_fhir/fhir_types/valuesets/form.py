from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirFormCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-forms.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirFormCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirFormCode']) -> None:
            self.f: Callable[..., 'FhirFormCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirFormCode']
        ) -> 'FhirFormCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirFormCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirFormCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/forms-codes"
