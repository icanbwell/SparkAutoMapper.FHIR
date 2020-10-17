from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperNumberInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept


class AutoMapperFhirDataTypeDiagnosisBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            sequence: AutoMapperNumberInputType,
            diagnosisCodeableConcept: AutoMapperFhirDataTypeCodeableConcept,
            type_: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            onAdmission: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            packageCode: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'AutoMapperFhirDataTypeDiagnosisBackboneElement':
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
        return AutoMapperFhirDataTypeDiagnosisBackboneElement(
            sequence=sequence,
            diagnosisCodeableConcept=diagnosisCodeableConcept,
            type_=type_,
            onAdmission=onAdmission,
            packageCode=packageCode
        )
