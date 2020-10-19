from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ProviderQualificationCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/v2/0360/2.7/index.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ProviderQualificationCode']
        ) -> None:
            self.f: Callable[..., 'ProviderQualificationCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ProviderQualificationCode']
        ) -> 'ProviderQualificationCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ProviderQualificationCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ProviderQualificationCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/ValueSet/v2-2.7-030"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return ""
