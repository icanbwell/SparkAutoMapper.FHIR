from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirClaimSubTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-subtype.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirClaimSubTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirClaimSubTypeCode']) -> None:
            self.f: Callable[..., 'FhirClaimSubTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirClaimSubTypeCode']
        ) -> 'FhirClaimSubTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirClaimSubTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirClaimSubTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-claimsubtype"
