from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirNote(AutoMapperDataTypeComplexBase):
    # noinspection SpellCheckingInspection
    @classmethod
    def map(cls,
            number: Optional[AutoMapperFhirPositiveIntInputType] = None,
            type_: Optional[AutoMapperFhirCodeInputType] = None,
            text: Optional[FhirString] = None,
            language: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'FhirNote':
        """
        Note Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.processNote


        :param number: Note instance identifier
        :param type_: display | print | printoper.  https://hl7.org/FHIR/valueset-note-type.html
        :param text: Note explanatory text
        :param language: Language of the text. https://hl7.org/FHIR/valueset-languages.html
        """
        return FhirNote(
            number=number,
            type_=type_,
            text=text,
            language=language
        )
