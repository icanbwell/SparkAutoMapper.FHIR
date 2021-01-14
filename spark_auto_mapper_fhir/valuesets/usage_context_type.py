from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class UsageContextTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-usage-context-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'UsageContextTypeCode']) -> None:
            self.f: Callable[..., 'UsageContextTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['UsageContextTypeCode']
        ) -> 'UsageContextTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'UsageContextTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return UsageContextTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/usage-context-type
        """
        return "http://hl7.org/fhir/ValueSet/usage-context-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.101
        """
        return "2.16.840.1.113883.4.642.3.101"
