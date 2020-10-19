from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirLinkTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-link-type.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirLinkTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirLinkTypeCode']) -> None:
            self.f: Callable[..., 'FhirLinkTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirLinkTypeCode']
        ) -> 'FhirLinkTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirLinkTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirLinkTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/link-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.423"
