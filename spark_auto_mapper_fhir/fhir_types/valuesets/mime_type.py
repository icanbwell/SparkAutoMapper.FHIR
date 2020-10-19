from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMimeTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-mimetypes.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirMimeTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirMimeTypeCode']) -> None:
            self.f: Callable[..., 'FhirMimeTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirMimeTypeCode']
        ) -> 'FhirMimeTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirMimeTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirMimeTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:ietf:bcp:13"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.1024"
