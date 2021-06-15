from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosisRole(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-diagnosis-role.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "DiagnosisRole"]) -> None:
            self.f: Callable[..., "DiagnosisRole"] = f

        def __get__(self, obj: Any, owner: Type["DiagnosisRole"]) -> "DiagnosisRole":
            return self.f(owner)

    @classproperty
    def AdmissionDiagnosis(cls) -> "DiagnosisRole":
        """
        Admission diagnosis
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("AD")

    @classproperty
    def DischargeDiagnosis(cls) -> "DiagnosisRole":
        """
        Discharge diagnosis
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("DD")

    @classproperty
    def ChiefComplaint(cls) -> "DiagnosisRole":
        """
        Chief complaint
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("CC")

    @classproperty
    def ComorbidityDiagnosis(cls) -> "DiagnosisRole":
        """
        Comorbidity diagnosis
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("CM")

    @classproperty
    def preOpDiagnosis(cls) -> "DiagnosisRole":
        """
        pre-op diagnosis
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("pre-op")

    @classproperty
    def postOpDiagnosis(cls) -> "DiagnosisRole":
        """
        post-op diagnosis
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("post-op")

    @classproperty
    def Billing(cls) -> "DiagnosisRole":
        """
        Billing
        """
        # noinspection PyCallingNonCallable
        return DiagnosisRole("billing")

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
