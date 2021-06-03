from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MimeTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-mimetypes.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MimeTypeCode"]) -> None:
            self.f: Callable[..., "MimeTypeCode"] = f

        def __get__(self, obj: Any, owner: Type["MimeTypeCode"]) -> "MimeTypeCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "MimeTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return MimeTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:ietf:bcp:13"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.1024"
