from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirProviderQualificationCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/v2/0360/2.7/index.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirProviderQualificationCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirProviderQualificationCode']
        ) -> None:
            self.f: Callable[..., 'FhirProviderQualificationCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirProviderQualificationCode']
        ) -> 'FhirProviderQualificationCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirProviderQualificationCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirProviderQualificationCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/ValueSet/v2-2.7-030"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return ""
