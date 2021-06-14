from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterSpecialArrangementCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-special-arrangements.html
    """

    def __init__(self, *, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterSpecialArrangementCode"]) -> None:
            self.f: Callable[..., "EncounterSpecialArrangementCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterSpecialArrangementCode"]
        ) -> "EncounterSpecialArrangementCode":
            return self.f(owner)

    @classproperty
    def WheelChair(cls) -> "EncounterSpecialArrangementCode":
        """
        The patient requires a wheelchair to be made available for the encounter.

        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialArrangementCode(value="wheel")

    @classproperty
    def AdditionalBedding(cls) -> "EncounterSpecialArrangementCode":
        """
        An additional bed made available for a person accompanying the patient, for example a parent accompanying a child.

        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialArrangementCode(value="add-bed")

    @classproperty
    def Interpreter(cls) -> "EncounterSpecialArrangementCode":
        """
        The patient is not fluent in the local language and requires an interpreter to be available. Refer to the Patient.Language property for the type of interpreter required.

        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialArrangementCode(value="int")

    @classproperty
    def Attendant(cls) -> "EncounterSpecialArrangementCode":
        """
        A person who accompanies a patient to provide assistive services necessary for the patient's care during the encounter.

        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialArrangementCode(value="att")

    @classproperty
    def GuideDog(cls) -> "EncounterSpecialArrangementCode":
        """
        The patient has a guide dog and the location used for the encounter should be able to support the presence of the service animal.

        """
        # noinspection PyCallingNonCallable
        return EncounterSpecialArrangementCode(value="dog")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-special-arrangements
        """
        return "http://hl7.org/fhir/ValueSet/encounter-special-arrangements"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.253
        """
        return "2.16.840.1.113883.4.642.3.253"
