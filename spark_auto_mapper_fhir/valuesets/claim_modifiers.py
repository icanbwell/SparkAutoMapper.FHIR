from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimModifiersCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-modifiers.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimModifiersCode"]) -> None:
            self.f: Callable[..., "ClaimModifiersCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ClaimModifiersCode"]
        ) -> "ClaimModifiersCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ClaimModifiersCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ClaimModifiersCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/modifiers"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.536"
