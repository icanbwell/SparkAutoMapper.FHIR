from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney


class FhirAdjudication(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            category: Optional[FhirCodeableConcept] = None,
            amount: Optional[FhirMoney] = None
            ) -> 'FhirAdjudication':
        """
        Adjudication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Adjudication
        Example: https://hl7.org/FHIR/explanationofbenefit-example.json.html

        :param category: category for adjudication
        :param amount: amount for adjudication
        """
        return FhirAdjudication(
            category=category,
            amount=amount
        )
