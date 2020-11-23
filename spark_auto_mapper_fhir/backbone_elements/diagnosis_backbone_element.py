from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.diagnosis_on_admission import DiagnosisOnAdmissionCode
from spark_auto_mapper_fhir.valuesets.diagnosis_related_group import DiagnosisRelatedGroupCode
from spark_auto_mapper_fhir.valuesets.diagnosis_type import DiagnosisTypeCode
from spark_auto_mapper_fhir.valuesets.icd_10 import Icd10Code
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class DiagnosisBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        diagnosisCodeableConcept: CodeableConcept[Icd10Code],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
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
            id_=id_,
            extension=extension,
            sequence=sequence,
            diagnosisCodeableConcept=diagnosisCodeableConcept,
            type_=type_,
            onAdmission=onAdmission,
            packageCode=packageCode
        )
