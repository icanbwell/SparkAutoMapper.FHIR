from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterAdmitSourceCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    http://hl7.org/fhir/ValueSet/encounter-admit-source
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterAdmitSourceCode"]) -> None:
            self.f: Callable[..., "EncounterAdmitSourceCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterAdmitSourceCode"]
        ) -> "EncounterAdmitSourceCode":
            return self.f(owner)

    @classproperty
    def HospTrans(cls) -> "EncounterAdmitSourceCode":
        """
        The Patient has been transferred from another hospital for this encounter.
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("hosp-trans")

    @classproperty
    def EMD(cls) -> "EncounterAdmitSourceCode":
        """
        From accident/emergency department
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("emd")

    @classproperty
    def OutPatient(cls) -> "EncounterAdmitSourceCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("outp")

    @classproperty
    def Born(cls) -> "EncounterAdmitSourceCode":
        """
        Born in hospital
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("born")

    @classproperty
    def GeneralPractitioner(cls) -> "EncounterAdmitSourceCode":
        """
        General Practitioner
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("gp")

    @classproperty
    def MedicalPractitioner(cls) -> "EncounterAdmitSourceCode":
        """
        Medical Practitioner/physician referral
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("mp")

    @classproperty
    def NursingHome(cls) -> "EncounterAdmitSourceCode":
        """
        From nursing home
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("nursing")

    @classproperty
    def PsychiatricHospital(cls) -> "EncounterAdmitSourceCode":
        """
        From psychiatric hospital
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("psych")

    @classproperty
    def Rehab(cls) -> "EncounterAdmitSourceCode":
        """
        From rehabilitation facility
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("rehab")

    @classproperty
    def Other(cls) -> "EncounterAdmitSourceCode":
        """
        Other
        """
        # noinspection PyCallingNonCallable
        return EncounterAdmitSourceCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-admit-source
        """
        return "http://hl7.org/fhir/ValueSet/encounter-admit-source"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.257
        """
        return "2.16.840.1.113883.4.642.3.257"
