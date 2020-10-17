from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.money import AutoMapperFhirDataTypeMoney


class AutoMapperFhirDataTypeAdjudication(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            category: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            amount: Optional[AutoMapperFhirDataTypeMoney] = None
            ) -> 'AutoMapperFhirDataTypeAdjudication':
        """
        Adjudication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Adjudication
        Example: https://hl7.org/FHIR/explanationofbenefit-example.json.html

        :param category: category for adjudication
        :param amount: amount for adjudication
        """
        return AutoMapperFhirDataTypeAdjudication(
            category=category,
            amount=amount
        )
