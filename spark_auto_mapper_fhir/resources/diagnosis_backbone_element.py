from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.diagnosis_on_admission import DiagnosisOnAdmissionCode
from spark_auto_mapper_fhir.valuesets.diagnosis_related_group import DiagnosisRelatedGroupCode
from spark_auto_mapper_fhir.valuesets.diagnosis_type import DiagnosisTypeCode
from spark_auto_mapper_fhir.valuesets.icd_10 import Icd10Code
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class DiagnosisBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        diagnosisCodeableConcept: CodeableConcept[Icd10Code],
        type_: Optional[CodeableConcept[DiagnosisTypeCode]] = None,
        onAdmission: Optional[CodeableConcept[DiagnosisOnAdmissionCode]
                              ] = None,
        packageCode: Optional[CodeableConcept[DiagnosisRelatedGroupCode]
                              ] = None
    ):
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
        super().__init__(
            sequence=sequence,
            diagnosisCodeableConcept=diagnosisCodeableConcept,
            type_=type_,
            onAdmission=onAdmission,
            packageCode=packageCode
        )
