from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.codes.adjudication import FhirAdjudicationCode
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney


class FhirTotalBackBoneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            category: FhirList[FhirCodeableConcept[FhirAdjudicationCode]],
            amount: FhirMoney
            ) -> 'FhirTotalBackBoneElement':
        """
        TotalBackBoneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.total


        :param category: Type of adjudication information. https://hl7.org/FHIR/valueset-adjudication.html
        :param amount: Financial total for the category
        """
        return FhirTotalBackBoneElement(
            category=category,
            amount=amount
        )
