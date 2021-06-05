from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CurrencyCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-currencies.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "CurrencyCode"]) -> None:
            self.f: Callable[..., "CurrencyCode"] = f

        def __get__(self, obj: Any, owner: Type["CurrencyCode"]) -> "CurrencyCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "CurrencyCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CurrencyCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:iso:std:iso:4217"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.1025"
