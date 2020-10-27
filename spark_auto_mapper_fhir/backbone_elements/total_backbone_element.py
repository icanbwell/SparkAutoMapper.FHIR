from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.adjudication import AdjudicationCode
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.money import Money


class TotalBackBoneElement(FhirBackboneElementBase):
    def __init__(
        self, category: FhirList[CodeableConcept[AdjudicationCode]],
        amount: Money
    ):
        """
        TotalBackBoneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.total


        :param category: Type of adjudication information. https://hl7.org/FHIR/valueset-adjudication.html
        :param amount: Financial total for the category
        """
        super().__init__(category=category, amount=amount)
