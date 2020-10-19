from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirContactPointSystemCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-contact-point-system.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirContactPointSystemCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirContactPointSystemCode']
        ) -> None:
            self.f: Callable[..., 'FhirContactPointSystemCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirContactPointSystemCode']
        ) -> 'FhirContactPointSystemCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirContactPointSystemCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirContactPointSystemCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/contact-point-system"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.71"
