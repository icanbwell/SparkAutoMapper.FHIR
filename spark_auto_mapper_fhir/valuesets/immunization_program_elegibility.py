from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationProgramElegibilityCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-program-eligibility.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., "ImmunizationProgramElegibilityCode"]
        ) -> None:
            self.f: Callable[..., "ImmunizationProgramElegibilityCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationProgramElegibilityCode"]
        ) -> "ImmunizationProgramElegibilityCode":
            return self.f(owner)

    @classproperty
    def NotEligible(cls) -> "ImmunizationProgramElegibilityCode":
        """
        The patient is not eligible for the funding program.
        """
        # noinspection PyCallingNonCallable
        return ImmunizationProgramElegibilityCode("ineligible")

    @classproperty
    def Uninsured(cls) -> "ImmunizationProgramElegibilityCode":
        """
        The patient is eligible for the funding program because they are uninsured
        """
        # noinspection PyCallingNonCallable
        return ImmunizationProgramElegibilityCode("uninsured")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-program-eligibility
        """
        return "http://hl7.org/fhir/ValueSet/immunization-program-eligibility"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.291
        """
        return "2.16.840.1.113883.4.642.3.291"
