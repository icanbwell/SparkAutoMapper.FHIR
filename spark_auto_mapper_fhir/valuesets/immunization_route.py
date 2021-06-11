from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ImmunizationRouteCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-immunization-route.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ImmunizationRouteCode"]) -> None:
            self.f: Callable[..., "ImmunizationRouteCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ImmunizationRouteCode"]
        ) -> "ImmunizationRouteCode":
            return self.f(owner)

    @classproperty
    def intradermal(cls) -> "ImmunizationRouteCode":
        """
        Injection, intradermal
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("IDINJ")

    @classproperty
    def intramuscular(cls) -> "ImmunizationRouteCode":
        """
        Injection, intramuscular
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("IM")

    @classproperty
    def Inhalation(cls) -> "ImmunizationRouteCode":
        """
        Inhalation, nasal, prongs
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("NASINHLC")

    @classproperty
    def Intravenous(cls) -> "ImmunizationRouteCode":
        """
        Injection, intravenous
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("IVINJ")

    @classproperty
    def oral(cls) -> "ImmunizationRouteCode":
        """
        Swallow, oral
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("PO")

    @classproperty
    def Subcutaneous(cls) -> "ImmunizationRouteCode":
        """
        Injection, subcutaneous
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("SQ")

    @classproperty
    def Transdermal(cls) -> "ImmunizationRouteCode":
        """
        Transdermal
        """
        # noinspection PyCallingNonCallable
        return ImmunizationRouteCode("TRNSDERM")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/immunization-route
        """
        return "http://hl7.org/fhir/ValueSet/immunization-route"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.289
        """
        return "2.16.840.1.113883.4.642.3.289"
