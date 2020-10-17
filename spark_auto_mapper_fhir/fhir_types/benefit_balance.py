from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.financial_benefit import FhirFinancialBenefit
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirBenefitBalance(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            category: AutoMapperFhirDataTypeCodeableConcept,
            excluded: Optional[FhirBoolean] = None,
            name: Optional[FhirString] = None,
            description: Optional[FhirString] = None,
            network: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            unit: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            term: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            financial: Optional[FhirList[FhirFinancialBenefit]] = None
            ) -> 'FhirBenefitBalance':
        """
        BenefitBalance Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.benefitBalance
        Balance by Benefit Category


        :param category: Benefit classification. https://hl7.org/FHIR/valueset-ex-benefitcategory.html
        :param excluded: Excluded from the plan
        :param name: Short name for the benefit
        :param description: Description of the benefit or services covered
        :param network: In or out of network. https://hl7.org/FHIR/valueset-benefit-network.html
        :param unit: Individual or family.  https://hl7.org/FHIR/valueset-benefit-unit.html
        :param term: Annual or lifetime. https://hl7.org/FHIR/valueset-benefit-term.html
        :param financial: Benefit Summary
        """
        return FhirBenefitBalance(
            category=category,
            excluded=excluded,
            name=name,
            description=description,
            network=network,
            unit=unit,
            term=term,
            financial=financial
        )
