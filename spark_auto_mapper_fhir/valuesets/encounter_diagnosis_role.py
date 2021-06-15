from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterDiagnosisRoleCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-diagnosis-role.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterDiagnosisRoleCode"]) -> None:
            self.f: Callable[..., "EncounterDiagnosisRoleCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterDiagnosisRoleCode"]
        ) -> "EncounterDiagnosisRoleCode":
            return self.f(owner)

    @classproperty
    def AdmissionDiagnosis(cls) -> "EncounterDiagnosisRoleCode":
        """
        Admission diagnosis
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("AD")

    @classproperty
    def DischargeDiagnosis(cls) -> "EncounterDiagnosisRoleCode":
        """
        Admission diagnosis
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("DD")

    @classproperty
    def ChiefComplaint(cls) -> "EncounterDiagnosisRoleCode":
        """
        Chief complaint
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("CC")

    @classproperty
    def ComorbidityDiagnosis(cls) -> "EncounterDiagnosisRoleCode":
        """
        Comorbidity diagnosis
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("CM")

    @classproperty
    def PreOp(cls) -> "EncounterDiagnosisRoleCode":
        """
        pre-op diagnosis
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("pre-op")

    @classproperty
    def PostOp(cls) -> "EncounterDiagnosisRoleCode":
        """
        Post-op diagnosis
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("post-op")

    @classproperty
    def Billing(cls) -> "EncounterDiagnosisRoleCode":
        """
        Billing
        """
        # noinspection PyCallingNonCallable
        return EncounterDiagnosisRoleCode("billing")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/diagnosis-role
        """
        return "http://hl7.org/fhir/ValueSet/diagnosis-role"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.49
        """
        return "2.16.840.1.113883.4.642.3.49"
