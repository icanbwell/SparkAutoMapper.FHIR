from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.benefit_category import BenefitCategoryCode
from spark_auto_mapper_fhir.fhir_types.valuesets.benefit_term import BenefitTermCode
from spark_auto_mapper_fhir.fhir_types.valuesets.benefit_unit_type import BenefitUnitTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.network_type import NetworkTypeCode
from spark_auto_mapper_fhir.fhir_types.financial_benefit import FhirFinancialBenefit
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirBenefitBalance(FhirResourceBase):
    def __init__(
        self,
        category: FhirCodeableConcept[BenefitCategoryCode],
        excluded: Optional[FhirBoolean] = None,
        name: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        network: Optional[FhirCodeableConcept[NetworkTypeCode]] = None,
        unit: Optional[FhirCodeableConcept[BenefitUnitTypeCode]] = None,
        term: Optional[FhirCodeableConcept[BenefitTermCode]] = None,
        financial: Optional[FhirList[FhirFinancialBenefit]] = None
    ):
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
        super().__init__(
            category=category,
            excluded=excluded,
            name=name,
            description=description,
            network=network,
            unit=unit,
            term=term,
            financial=financial
        )
