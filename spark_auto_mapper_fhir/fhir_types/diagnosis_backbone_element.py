from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_on_admission import DiagnosisOnAdmissionCode
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_related_group import DiagnosisRelatedGroupCode
from spark_auto_mapper_fhir.fhir_types.valuesets.diagnosis_type import DiagnosisTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.icd_10 import Icd10Code
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class FhirDiagnosisBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        diagnosisCodeableConcept: FhirCodeableConcept[Icd10Code],
        type_: Optional[FhirCodeableConcept[DiagnosisTypeCode]] = None,
        onAdmission: Optional[FhirCodeableConcept[DiagnosisOnAdmissionCode]
                              ] = None,
        packageCode: Optional[FhirCodeableConcept[DiagnosisRelatedGroupCode]
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
