from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirClaimTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-type.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirClaimTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirClaimTypeCode']) -> None:
            self.f: Callable[..., 'FhirClaimTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirClaimTypeCode']
        ) -> 'FhirClaimTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirClaimTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirClaimTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://hl7.org/FHIR/codesystem-claim-type.html"
