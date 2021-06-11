from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationSiteCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-site.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationSiteCode"]) -> None:
            self.f: Callable[..., "ImmunizationSiteCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationSiteCode"]
        ) -> "ImmunizationSiteCode":
            return self.f(owner)

    @classproperty
    def LeftArm(cls) -> "ImmunizationSiteCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ImmunizationSiteCode("LA")

    @classproperty
    def RightArm(cls) -> "ImmunizationSiteCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ImmunizationSiteCode("RA")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-site
        """
        return "http://hl7.org/fhir/ValueSet/immunization-site"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.288
        """
        return "2.16.840.1.113883.4.642.3.288"
