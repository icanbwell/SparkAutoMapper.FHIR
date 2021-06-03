from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosisTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-ex-diagnosistype.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "DiagnosisTypeCode"]) -> None:
            self.f: Callable[..., "DiagnosisTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["DiagnosisTypeCode"]
        ) -> "DiagnosisTypeCode":
            return self.f(owner)

    @classproperty
    def AdmittingDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        The diagnosis given as the reason why the patient was admitted to the hospital.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("admitting")

    def ClinicalDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis made on the basis of medical signs and patient-reported symptoms, rather than diagnostic tests.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("clinical")

    def DifferentialDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        One of a set of the possible diagnoses that could be connected to the signs, symptoms, and lab findings.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("differential")

    def DischargeDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        The diagnosis given when the patient is discharged from the hospital.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("discharge")

    def LaboratoryDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis based significantly on laboratory reports or test results, rather than the physical examination of the patient.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("laboratory")

    def NursingDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis which identifies people's responses to situations in their lives, such as a readiness to change or a willingness to accept assistance.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("nursing")

    def PrenatalDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis determined prior to birth.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("prenatal")

    def PrincipalDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        The single medical diagnosis that is most relevant to the patient's chief complaint or need for treatment.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("principal")

    def RadiologyDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis based primarily on the results from medical imaging studies.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("radiology")

    def RemoteDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis determined using telemedicine techniques.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("remote")

    def RetrospectiveDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        The labeling of an illness in a specific historical event using modern knowledge, methods and disease classifications.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("retrospective")

    def SelfDiagnosis(cls) -> "DiagnosisTypeCode":
        """
        A diagnosis determined by the patient.
        """
        # noinspection PyCallingNonCallable
        return DiagnosisTypeCode("self")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-diagnosistype"
