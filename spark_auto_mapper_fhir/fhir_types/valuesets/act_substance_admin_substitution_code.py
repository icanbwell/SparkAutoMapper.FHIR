from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

# noinspection PyMethodParameters
# noinspection PyPep8Naming
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


class FhirActSubstanceAdminSubstitutionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirActSubstanceAdminSubstitutionCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirActSubstanceAdminSubstitutionCode']
        ) -> None:
            self.f: Callable[..., 'FhirActSubstanceAdminSubstitutionCode'] = f

        def __get__(
            self, obj: Any,
            owner: Type['FhirActSubstanceAdminSubstitutionCode']
        ) -> 'FhirActSubstanceAdminSubstitutionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirActSubstanceAdminSubstitutionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirActSubstanceAdminSubstitutionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubstitution"
