from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterDischargeDispositionCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-discharge-disposition.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., "EncounterDischargeDispositionCode"]
        ) -> None:
            self.f: Callable[..., "EncounterDischargeDispositionCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterDischargeDispositionCode"]
        ) -> "EncounterDischargeDispositionCode":
            return self.f(owner)

    @classproperty
    def Home(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient was dicharged and has indicated that they are going to return home afterwards.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("home")

    @classproperty
    def AlternativeHome(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient was discharged and has indicated that they are going to return home afterwards, but not the patient's home - e.g. a family member's home.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("alt-home")

    @classproperty
    def OtherHealthcareFacility(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient was transferred to another healthcare facility.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("other-hcf")

    @classproperty
    def Hospice(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient has been discharged into palliative care.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("hosp")

    @classproperty
    def LongTermCare(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient has been discharged into long-term care where is likely to be monitored through an ongoing episode-of-care.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("long")

    @classproperty
    def LeftAgainstAdvice(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient self discharged against medical advice.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("aadvice")

    @classproperty
    def Expired(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient has deceased during this encounter.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("exp")

    @classproperty
    def PsychiatricHospital(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient has been transferred to a psychiatric facility.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("psy")

    @classproperty
    def Rehabilitation(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient was discharged and is to receive post acute care rehabilitation services.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("rehab")

    @classproperty
    def SkilledNursingFacility(cls) -> "EncounterDischargeDispositionCode":
        """
        The patient has been discharged to a skilled nursing facility for the patient to receive additional care.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("snf")

    @classproperty
    def Other(cls) -> "EncounterDischargeDispositionCode":
        """
        The discharge disposition has not otherwise defined.

        """
        # noinspection PyCallingNonCallable
        return EncounterDischargeDispositionCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-discharge-disposition
        """
        return "http://hl7.org/fhir/ValueSet/encounter-discharge-disposition"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.259
        """
        return "2.16.840.1.113883.4.642.3.259"
