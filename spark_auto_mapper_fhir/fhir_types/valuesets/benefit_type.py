from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirBenefitTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-benefit-type.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirBenefitTypeCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirBenefitTypeCode']) -> None:
            self.f: Callable[..., 'FhirBenefitTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirBenefitTypeCode']
        ) -> 'FhirBenefitTypeCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirBenefitTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirBenefitTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/benefit-type"
