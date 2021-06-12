from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ParticipantRequiredCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-participantrequired.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ParticipantRequiredCode"]) -> None:
            self.f: Callable[..., "ParticipantRequiredCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ParticipantRequiredCode"]
        ) -> "ParticipantRequiredCode":
            return self.f(owner)

    @classproperty
    def Required(cls) -> "ParticipantRequiredCode":
        """
        The participant is required to attend the appointment.
        """
        # noinspection PyCallingNonCallable
        return ParticipantRequiredCode("required")

    @classproperty
    def Optional(cls) -> "ParticipantRequiredCode":
        """
        The participant may optionally attend the appointment.
        """
        # noinspection PyCallingNonCallable
        return ParticipantRequiredCode("optional")

    @classproperty
    def InformationOnly(cls) -> "ParticipantRequiredCode":
        """
        The participant is excluded from the appointment, and might not be informed of the appointment taking place. (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).
        """
        # noinspection PyCallingNonCallable
        return ParticipantRequiredCode("information-only")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/participantrequired
        """
        return "http://hl7.org/fhir/ValueSet/participantrequired"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.488
        """
        return "2.16.840.1.113883.4.642.3.488"
