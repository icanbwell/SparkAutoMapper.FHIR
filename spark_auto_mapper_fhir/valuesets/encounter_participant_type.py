from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterParticipantTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-encounter-participant-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterParticipantTypeCode"]) -> None:
            self.f: Callable[..., "EncounterParticipantTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterParticipantTypeCode"]
        ) -> "EncounterParticipantTypeCode":
            return self.f(owner)

    @classproperty
    def NameYourFirstValue(cls) -> "EncounterParticipantTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return EncounterParticipantTypeCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-participant-type
        """
        return "http://hl7.org/fhir/ValueSet/encounter-participant-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.250
        """
        return "2.16.840.1.113883.4.642.3.250"
