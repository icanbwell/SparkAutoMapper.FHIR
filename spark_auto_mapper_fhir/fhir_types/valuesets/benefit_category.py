from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirBenefitCategoryCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-benefitcategory.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirBenefitCategoryCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirBenefitCategoryCode']
        ) -> None:
            self.f: Callable[..., 'FhirBenefitCategoryCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirBenefitCategoryCode']
        ) -> 'FhirBenefitCategoryCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirBenefitCategoryCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirBenefitCategoryCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-benefitcategory"
