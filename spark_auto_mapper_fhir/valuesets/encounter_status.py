from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterStatusCode"]) -> None:
            self.f: Callable[..., "EncounterStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterStatusCode"]
        ) -> "EncounterStatusCode":
            return self.f(owner)

    @classproperty
    def Planned(cls) -> "EncounterStatusCode":
        """
        The Encounter has not yet started.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("planned")

    @classproperty
    def Arrived(cls) -> "EncounterStatusCode":
        """
        The Patient is present for the encounter, however is not currently meeting with a practitioner.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("arrived")

    @classproperty
    def Triaged(cls) -> "EncounterStatusCode":
        """
        The patient has been assessed for the priority of their treatment based on the severity of their condition.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("triaged")

    @classproperty
    def InProgress(cls) -> "EncounterStatusCode":
        """
        The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("in-progress")

    @classproperty
    def OnLeave(cls) -> "EncounterStatusCode":
        """
        The Encounter has begun, but the patient is temporarily on leave.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("onleave")

    @classproperty
    def Finished(cls) -> "EncounterStatusCode":
        """
        The Encounter has ended.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("finished")

    @classproperty
    def Cancelled(cls) -> "EncounterStatusCode":
        """
        The Encounter has ended before it has begun.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("cancelled")

    @classproperty
    def EnteredInError(cls) -> "EncounterStatusCode":
        """
        This instance should not have been part of this patient's medical record.
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("entered-in-error")

    @classproperty
    def Unknown(cls) -> "EncounterStatusCode":
        """
        The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made to provide a meaningful value other than "unknown".
        """
        # noinspection PyCallingNonCallable
        return EncounterStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-status
        """
        return "http://hl7.org/fhir/ValueSet/encounter-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.246
        """
        return "2.16.840.1.113883.4.642.3.246"
