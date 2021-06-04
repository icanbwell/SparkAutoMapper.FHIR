from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode
from spark_auto_mapper_fhir.valuesets.note_type import NoteTypeCode
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Note(FhirComplexTypeBase):
    # noinspection SpellCheckingInspection
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        number: Optional[FhirPositiveInt] = None,
        type_: Optional[NoteTypeCode] = None,
        text: Optional[FhirString] = None,
        language: Optional[CodeableConcept[CommonLanguageCode]] = None,
    ):
        """
        Note Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.processNote


        :param number: Note instance identifier
        :param type_: display | print | printoper.  https://hl7.org/FHIR/valueset-note-type.html
        :param text: Note explanatory text
        :param language: Language of the text. https://hl7.org/FHIR/valueset-languages.html
        """
        super().__init__(
            id_=id_,
            extension=extension,
            number=number,
            type_=type_,
            text=text,
            language=language,
        )
