from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class AppointmentStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-appointmentstatus.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "AppointmentStatusCode"]) -> None:
            self.f: Callable[..., "AppointmentStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["AppointmentStatusCode"]
        ) -> "AppointmentStatusCode":
            return self.f(owner)

    @classproperty
    def Proposed(cls) -> "AppointmentStatusCode":
        """
        None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time might not be set yet.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("proposed")

    @classproperty
    def Pending(cls) -> "AppointmentStatusCode":
        """
        Some or all of the participant(s) have not finalized their acceptance of the appointment request.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("pending")

    @classproperty
    def Booked(cls) -> "AppointmentStatusCode":
        """
        All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times specified.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("booked")

    @classproperty
    def Arrived(cls) -> "AppointmentStatusCode":
        """
        The patient/patients has/have arrived and is/are waiting to be seen.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("arrived")

    @classproperty
    def Fulfilled(cls) -> "AppointmentStatusCode":
        """
        The planning stages of the appointment are now complete, the encounter resource will exist and will track further status changes. Note that an encounter may exist before the appointment status is fulfilled for many reasons.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("fulfilled")

    @classproperty
    def Cancelled(cls) -> "AppointmentStatusCode":
        """
        The appointment has been cancelled.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("cancelled")

    @classproperty
    def NoShow(cls) -> "AppointmentStatusCode":
        """
        Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("noshow")

    @classproperty
    def EnteredInError(cls) -> "AppointmentStatusCode":
        """
        This instance should not have been part of this patient's medical record.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("entered-in-error")

    @classproperty
    def CheckedIn(cls) -> "AppointmentStatusCode":
        """
        When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple patients are involved, they are all present).
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("checked-in")

    @classproperty
    def Waitlisted(cls) -> "AppointmentStatusCode":
        """
        The appointment has been placed on a waitlist, to be scheduled/confirmed in the future when a slot/service is available. A specific time might or might not be pre-allocated.
        """
        # noinspection PyCallingNonCallable
        return AppointmentStatusCode("waitlisted")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/appointmentstatus
        """
        return "http://hl7.org/fhir/ValueSet/appointmentstatus"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.484
        """
        return "2.16.840.1.113883.4.642.3.484"
