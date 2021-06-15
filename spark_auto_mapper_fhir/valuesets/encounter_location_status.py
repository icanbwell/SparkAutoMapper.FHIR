from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterLocationStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-location-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterLocationStatusCode"]) -> None:
            self.f: Callable[..., "EncounterLocationStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterLocationStatusCode"]
        ) -> "EncounterLocationStatusCode":
            return self.f(owner)

    @classproperty
    def Planned(cls) -> "EncounterLocationStatusCode":
        """
        The patient is planned to be moved to this location at some point in the future.
        """
        # noinspection PyCallingNonCallable
        return EncounterLocationStatusCode("planned")

    @classproperty
    def Active(cls) -> "EncounterLocationStatusCode":
        """
        The patient is currently at this location, or was between the period specified. A system may update these records when the patient leaves the location to either reserved, or completed.
        """
        # noinspection PyCallingNonCallable
        return EncounterLocationStatusCode("active")

    @classproperty
    def Reserved(cls) -> "EncounterLocationStatusCode":
        """
        This location is held empty for this patient.
        """
        # noinspection PyCallingNonCallable
        return EncounterLocationStatusCode("reserved")

    @classproperty
    def Completed(cls) -> "EncounterLocationStatusCode":
        """
        The patient was at this location during the period specified. Not to be used when the patient is currently at the location.
        """
        # noinspection PyCallingNonCallable
        return EncounterLocationStatusCode("completed")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-location-status
        """
        return "http://hl7.org/fhir/ValueSet/encounter-location-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.262
        """
        return "2.16.840.1.113883.4.642.3.262"
