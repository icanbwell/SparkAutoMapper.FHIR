from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ContactEntityTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-contactentity-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ContactEntityTypeCode"]) -> None:
            self.f: Callable[..., "ContactEntityTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ContactEntityTypeCode"]
        ) -> "ContactEntityTypeCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ContactEntityTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ContactEntityTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/contactentity-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.416"
