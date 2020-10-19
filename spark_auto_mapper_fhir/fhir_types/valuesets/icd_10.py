from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirIcd10Code(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-icd-10.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirIcd10Code':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirIcd10Code']) -> None:
            self.f: Callable[..., 'FhirIcd10Code'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirIcd10Code']
        ) -> 'FhirIcd10Code':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirIcd10Code':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirIcd10Code("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/sid/icd-10"
