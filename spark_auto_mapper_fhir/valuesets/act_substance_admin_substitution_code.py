from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActSubstanceAdminSubstitutionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ActSubstanceAdminSubstitutionCode']
        ) -> None:
            self.f: Callable[..., 'ActSubstanceAdminSubstitutionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ActSubstanceAdminSubstitutionCode']
        ) -> 'ActSubstanceAdminSubstitutionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ActSubstanceAdminSubstitutionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ActSubstanceAdminSubstitutionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-substanceAdminSubstitution"
