from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ParticipationStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-participationstatus.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ParticipationStatusCode"]) -> None:
            self.f: Callable[..., "ParticipationStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ParticipationStatusCode"]
        ) -> "ParticipationStatusCode":
            return self.f(owner)

    @classproperty
    def Accepted(cls) -> "ParticipationStatusCode":
        """
        The participant has accepted the appointment.
        """
        # noinspection PyCallingNonCallable
        return ParticipationStatusCode("accepted")

    @classproperty
    def Declined(cls) -> "ParticipationStatusCode":
        """
        The participant has declined the appointment and will not participate in the appointment.
        """
        # noinspection PyCallingNonCallable
        return ParticipationStatusCode("declined")

    @classproperty
    def Tentative(cls) -> "ParticipationStatusCode":
        """
        The participant has tentatively accepted the appointment. This could be automatically created by a system and requires further processing before it can be accepted. There is no commitment that attendance will occur.
        """
        # noinspection PyCallingNonCallable
        return ParticipationStatusCode("tentative")

    @classproperty
    def NeedsAction(cls) -> "ParticipationStatusCode":
        """
        The participant needs to indicate if they accept the appointment by changing this status to one of the other statuses.
        """
        # noinspection PyCallingNonCallable
        return ParticipationStatusCode("needs-action")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/participationstatus
        """
        return "http://hl7.org/fhir/ValueSet/participationstatus"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.486
        """
        return "2.16.840.1.113883.4.642.3.486"
