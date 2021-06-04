from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.benefit_category import BenefitCategoryCode
from spark_auto_mapper_fhir.valuesets.benefit_term import BenefitTermCode
from spark_auto_mapper_fhir.valuesets.benefit_unit_type import BenefitUnitTypeCode
from spark_auto_mapper_fhir.valuesets.network_type import NetworkTypeCode
from spark_auto_mapper_fhir.complex_types.financial_benefit import FinancialBenefit
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class BenefitBalance(FhirComplexTypeBase):
    def __init__(
        self,
        category: CodeableConcept[BenefitCategoryCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        excluded: Optional[FhirBoolean] = None,
        name: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        network: Optional[CodeableConcept[NetworkTypeCode]] = None,
        unit: Optional[CodeableConcept[BenefitUnitTypeCode]] = None,
        term: Optional[CodeableConcept[BenefitTermCode]] = None,
        financial: Optional[FhirList[FinancialBenefit]] = None,
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
            id_=id_,
            extension=extension,
            excluded=excluded,
            name=name,
            description=description,
            network=network,
            unit=unit,
            term=term,
            financial=financial,
        )
