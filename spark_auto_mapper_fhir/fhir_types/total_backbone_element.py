from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.adjudication import FhirAdjudicationCode
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney


class FhirTotalBackBoneElement(FhirResourceBase):
    @classmethod
    def map(
        cls, category: FhirList[FhirCodeableConcept[FhirAdjudicationCode]],
        amount: FhirMoney
    ) -> 'FhirTotalBackBoneElement':
        """
        TotalBackBoneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.total


        :param category: Type of adjudication information. https://hl7.org/FHIR/valueset-adjudication.html
        :param amount: Financial total for the category
        """
        return FhirTotalBackBoneElement(category=category, amount=amount)
