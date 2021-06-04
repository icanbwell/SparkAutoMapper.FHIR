from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class PublicationStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-publication-status.html
    draft | active | retired | unknown
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "PublicationStatusCode"]) -> None:
            self.f: Callable[..., "PublicationStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["PublicationStatusCode"]
        ) -> "PublicationStatusCode":
            return self.f(owner)

    @classproperty
    def Draft(cls) -> "PublicationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PublicationStatusCode("draft")

    @classproperty
    def Active(cls) -> "PublicationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PublicationStatusCode("active")

    @classproperty
    def Retired(cls) -> "PublicationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PublicationStatusCode("retired")

    @classproperty
    def Unknown(cls) -> "PublicationStatusCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return PublicationStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/publication-status
        """
        return "http://hl7.org/fhir/publication-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.3
        """
        return "2.16.840.1.113883.4.642.3.3"
