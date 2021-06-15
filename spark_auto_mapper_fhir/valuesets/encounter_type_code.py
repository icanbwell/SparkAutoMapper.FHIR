from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterTypeCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterTypeCode"]) -> None:
            self.f: Callable[..., "EncounterTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterTypeCode"]
        ) -> "EncounterTypeCode":
            return self.f(owner)

    @classproperty
    def AnnualDiabetes(cls) -> "EncounterTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EncounterTypeCode("ADMS")

    @classproperty
    def BoneDrilling(cls) -> "EncounterTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EncounterTypeCode("BD/BM-clin")

    @classproperty
    def OutpatientKenacort(cls) -> "EncounterTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EncounterTypeCode("OKI")

    @classproperty
    def InfantColonScreening(cls) -> "EncounterTypeCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EncounterTypeCode("CCS60")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-type
        """
        return "http://hl7.org/fhir/ValueSet/encounter-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        https://hl7.org/FHIR/valueset-encounter-type.html
        """
        return "https://hl7.org/FHIR/valueset-encounter-type.html"
