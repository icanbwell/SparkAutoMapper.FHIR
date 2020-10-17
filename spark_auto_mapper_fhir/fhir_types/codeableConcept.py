from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.coding import AutoMapperFhirDataTypeCoding


# noinspection SpellCheckingInspection
class AutoMapperFhirDataTypeCodeableConcept(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            coding: Optional[AutoMapperFhirDataTypeCoding] = None,
            text: Optional[AutoMapperTextInputType] = None
            ) -> 'AutoMapperFhirDataTypeCodeableConcept':
        """
        CodeableConcept Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CodeableConcept


        :param coding: Code defined by a terminology system
        :param text: Plain text representation of the concept
        """
        return AutoMapperFhirDataTypeCodeableConcept(
            coding=coding,
            text=text
        )
