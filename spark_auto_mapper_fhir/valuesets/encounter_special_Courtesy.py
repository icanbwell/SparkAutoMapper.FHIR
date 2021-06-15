from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterSpecialCourtesyCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-special-courtesy.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterSpecialCourtesyCode"]) -> None:
            self.f: Callable[..., "EncounterSpecialCourtesyCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterSpecialCourtesyCode"]
        ) -> "EncounterSpecialCourtesyCode":
            return self.f(owner)

    @classproperty
    def VIP(cls) -> "EncounterSpecialCourtesyCode":
        """
        VIP
        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialCourtesyCode("VIP")

    @classproperty
    def ExtendedCourtesy(cls) -> "EncounterSpecialCourtesyCode":
        """
        extended courtesy
        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialCourtesyCode("EXT")

    @classproperty
    def NormalCourtesy(cls) -> "EncounterSpecialCourtesyCode":
        """
        Normal Courtesy
        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialCourtesyCode("NRM")

    @classproperty
    def ProfessionalCourtesy(cls) -> "EncounterSpecialCourtesyCode":
        """
        professional courtesy
        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialCourtesyCode("PRF")

    @classproperty
    def Staff(cls) -> "EncounterSpecialCourtesyCode":
        """
        Courtesies extended to the staff of the entity providing service.
        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialCourtesyCode("STF")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-special-courtesy
        """
        return "http://hl7.org/fhir/ValueSet/encounter-special-courtesy"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.252
        """
        return "2.16.840.1.113883.4.642.3.252"
