from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt


class FhirDosage(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            sequence: Optional[FhirPositiveInt] = None,
            text: Optional[AutoMapperTextInputType] = None,
            additionalInstruction: Optional[FhirCodeableConcept] = None,
            patientInstruction: Optional[AutoMapperTextInputType] = None,
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
