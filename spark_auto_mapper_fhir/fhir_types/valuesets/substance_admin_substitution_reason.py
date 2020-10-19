from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirSubstanceAdminSubstitutionReason(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirSubstanceAdminSubstitutionReason':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirSubstanceAdminSubstitutionReason']
        ) -> None:
            self.f: Callable[..., 'FhirSubstanceAdminSubstitutionReason'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirSubstanceAdminSubstitutionReason']
        ) -> 'FhirSubstanceAdminSubstitutionReason':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirSubstanceAdminSubstitutionReason':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirSubstanceAdminSubstitutionReason("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-ActReason"
