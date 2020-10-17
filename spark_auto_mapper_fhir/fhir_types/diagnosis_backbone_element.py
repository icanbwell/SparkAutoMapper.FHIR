from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class FhirDiagnosisBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            sequence: FhirPositiveInt,
            diagnosisCodeableConcept: FhirCodeableConcept,
            type_: Optional[FhirCodeableConcept] = None,
            onAdmission: Optional[FhirCodeableConcept] = None,
            packageCode: Optional[FhirCodeableConcept] = None
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
