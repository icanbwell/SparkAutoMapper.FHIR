from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ConformanceUseContextCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-use-context.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ConformanceUseContextCode']
        ) -> None:
            self.f: Callable[..., 'ConformanceUseContextCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ConformanceUseContextCode']
        ) -> 'ConformanceUseContextCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ConformanceUseContextCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ConformanceUseContextCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/use-context
        """
        return "http://hl7.org/fhir/ValueSet/use-context"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.28
        """
        return "2.16.840.1.113883.4.642.3.28"
