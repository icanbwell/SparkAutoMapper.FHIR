from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class IdentityAssuranceLevelCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-identity-assuranceLevel.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "IdentityAssuranceLevelCode"]) -> None:
            self.f: Callable[..., "IdentityAssuranceLevelCode"] = f

        def __get__(
            self, obj: Any, owner: Type["IdentityAssuranceLevelCode"]
        ) -> "IdentityAssuranceLevelCode":
            return self.f(owner)

    @classproperty
    def Level1(cls) -> "IdentityAssuranceLevelCode":
        """
        Little or no confidence in the asserted identity's accuracy.
        """
        # noinspection PyCallingNonCallable
        return IdentityAssuranceLevelCode("level1")

    @classproperty
    def Level2(cls) -> "IdentityAssuranceLevelCode":
        """
        Some confidence in the asserted identity's accuracy.
        """
        # noinspection PyCallingNonCallable
        return IdentityAssuranceLevelCode("level2")

    @classproperty
    def Level3(cls) -> "IdentityAssuranceLevelCode":
        """
        High confidence in the asserted identity's accuracy.
        """
        # noinspection PyCallingNonCallable
        return IdentityAssuranceLevelCode("level3")

    @classproperty
    def Level4(cls) -> "IdentityAssuranceLevelCode":
        """
        Very high confidence in the asserted identity's accuracy.
        """
        # noinspection PyCallingNonCallable
        return IdentityAssuranceLevelCode("level4")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/identity-assuranceLevel"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.656"
