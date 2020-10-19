from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.additional_dosage_instruction import FhirAdditionalDosageInstructionCode
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirDosage(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        sequence: Optional[FhirPositiveInt] = None,
        text: Optional[FhirString] = None,
        additionalInstruction: Optional[
            FhirCodeableConcept[FhirAdditionalDosageInstructionCode]] = None,
        patientInstruction: Optional[FhirString] = None,
    ) -> 'FhirDosage':
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
        return FhirDosage(
            sequence=sequence,
            text=text,
            additionalInstruction=additionalInstruction,
            patientInstruction=patientInstruction
        )
