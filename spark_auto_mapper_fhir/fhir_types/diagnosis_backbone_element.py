from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_on_admission import FhirDiagnosisOnAdmissionCode
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_related_group import FhirDiagnosisRelatedGroupCode
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_type import FhirDiagnosisType
from spark_auto_mapper_fhir.fhir_types.valuesets.icd_10 import FhirIcd10Code
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class FhirDiagnosisBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(
        cls,
        sequence: FhirPositiveInt,
        diagnosisCodeableConcept: FhirCodeableConcept[FhirIcd10Code],
        type_: Optional[FhirCodeableConcept[FhirDiagnosisType]] = None,
        onAdmission: Optional[FhirCodeableConcept[FhirDiagnosisOnAdmissionCode]
                              ] = None,
        packageCode: Optional[
            FhirCodeableConcept[FhirDiagnosisRelatedGroupCode]] = None
    ) -> 'FhirDiagnosisBackboneElement':
        """
        DiagnosisBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DiagnosisBackboneElement
        https://hl7.org/FHIR/explanationofbenefit.html


        :param sequence: Diagnosis instance identifier
        :param diagnosisCodeableConcept: Nature of illness or problem https://hl7.org/FHIR/valueset-icd-10.html
        :param type_: Timing or nature of the diagnosis https://hl7.org/FHIR/valueset-ex-diagnosistype.html
        :param onAdmission: Present on admission https://hl7.org/FHIR/valueset-ex-diagnosis-on-admission.html
        :param packageCode: Package billing code https://hl7.org/FHIR/valueset-ex-diagnosisrelatedgroup.html
        """
        return FhirDiagnosisBackboneElement(
            sequence=sequence,
            diagnosisCodeableConcept=diagnosisCodeableConcept,
            type_=type_,
            onAdmission=onAdmission,
            packageCode=packageCode
        )
