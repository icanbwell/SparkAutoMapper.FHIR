from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ClaimTypeCode']) -> None:
            self.f: Callable[..., 'ClaimTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ClaimTypeCode']
        ) -> 'ClaimTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ClaimTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://hl7.org/FHIR/codesystem-claim-type.html"
