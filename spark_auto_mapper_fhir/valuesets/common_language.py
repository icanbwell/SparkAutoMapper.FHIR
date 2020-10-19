from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CommonLanguageCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-languages.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'CommonLanguageCode']) -> None:
            self.f: Callable[..., 'CommonLanguageCode'] = f

        def __get__(
            self, obj: Any, owner: Type['CommonLanguageCode']
        ) -> 'CommonLanguageCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'CommonLanguageCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CommonLanguageCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:ietf:bcp:47"
