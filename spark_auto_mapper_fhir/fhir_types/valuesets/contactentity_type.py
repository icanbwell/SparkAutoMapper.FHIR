from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirContactEntityTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-contactentity-type.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirContactEntityTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirContactEntityTypeCode']
        ) -> None:
            self.f: Callable[..., 'FhirContactEntityTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirContactEntityTypeCode']
        ) -> 'FhirContactEntityTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirContactEntityTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirContactEntityTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/contactentity-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.416"
