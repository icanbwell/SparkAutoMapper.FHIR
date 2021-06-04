from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ContactPointSystemCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-contact-point-system.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ContactPointSystemCode"]) -> None:
            self.f: Callable[..., "ContactPointSystemCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ContactPointSystemCode"]
        ) -> "ContactPointSystemCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ContactPointSystemCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ContactPointSystemCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/contact-point-system"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.71"
