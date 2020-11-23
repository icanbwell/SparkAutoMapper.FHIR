from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.additional_dosage_instruction import AdditionalDosageInstructionCode
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Dosage(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        sequence: Optional[FhirPositiveInt] = None,
        text: Optional[FhirString] = None,
        additionalInstruction: Optional[
            CodeableConcept[AdditionalDosageInstructionCode]] = None,
        patientInstruction: Optional[FhirString] = None,
    ):
        """
        Dosage Resource in FHIR
        https://hl7.org/FHIR/dosage.html#Dosage
        How the medication is/was taken or should be taken

        :param sequence: The order of the dosage instructions
        :param text: Free text dosage instructions e.g. SIG
        :param additionalInstruction: Supplemental instruction or warnings to the patient -
                                        e.g. "with meals", "may cause drowsiness".
                                        https://hl7.org/FHIR/valueset-additional-instruction-codes.html
        :param patientInstruction: Patient or consumer oriented instructions
        """
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            text=text,
            additionalInstruction=additionalInstruction,
            patientInstruction=patientInstruction
        )
