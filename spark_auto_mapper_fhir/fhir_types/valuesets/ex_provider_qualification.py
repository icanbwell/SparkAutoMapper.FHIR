from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirExProviderQualificationCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-provider-qualification.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirExProviderQualificationCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirExProviderQualificationCode']
        ) -> None:
            self.f: Callable[..., 'FhirExProviderQualificationCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirExProviderQualificationCode']
        ) -> 'FhirExProviderQualificationCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirExProviderQualificationCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirExProviderQualificationCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-providerqualification"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.570"
