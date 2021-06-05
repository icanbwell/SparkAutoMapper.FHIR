from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionParticipantTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-participant-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionParticipantTypeCode"]) -> None:
            self.f: Callable[..., "ActionParticipantTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionParticipantTypeCode"]
        ) -> "ActionParticipantTypeCode":
            return self.f(owner)

    @classproperty
    def Patient(cls) -> "ActionParticipantTypeCode":
        """
        The participant is the patient under evaluation.
        """
        # noinspection PyCallingNonCallable
        return ActionParticipantTypeCode("patient")

    @classproperty
    def Practitioner(cls) -> "ActionParticipantTypeCode":
        """
        The participant is a practitioner involved in the patient's care.
        """
        # noinspection PyCallingNonCallable
        return ActionParticipantTypeCode("practitioner")

    @classproperty
    def RelatedPerson(cls) -> "ActionParticipantTypeCode":
        """
        The participant is a person related to the patient.
        """
        # noinspection PyCallingNonCallable
        return ActionParticipantTypeCode("related-person")

    @classproperty
    def Device(cls) -> "ActionParticipantTypeCode":
        """
        The participant is a system or device used in the care of the patient.
        """
        # noinspection PyCallingNonCallable
        return ActionParticipantTypeCode("device")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-participant-type
        """
        return "http://hl7.org/fhir/ValueSet/action-participant-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.811
        """
        return "2.16.840.1.113883.4.642.3.811"
