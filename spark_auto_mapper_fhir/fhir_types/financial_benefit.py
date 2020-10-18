from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.money import FhirMoney
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


class FhirFinancialBenefit(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            type_: Optional[FhirCodeableConcept] = None,
            allowedUnsignedInt: Optional[FhirUnsignedInt] = None,
            allowedString: Optional[FhirString] = None,
            allowedMoney: Optional[FhirMoney] = None,
            usedUnsignedInt: Optional[FhirUnsignedInt] = None,
            usedMoney: Optional[FhirMoney] = None
            ) -> 'FhirFinancialBenefit':
        """
        FinancialBenefit Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.benefitBalance.financial
        Benefit Summary


        :param type_: Benefit classification. https://hl7.org/FHIR/valueset-benefit-type.html
        :param allowedUnsignedInt: Benefits allowed
        :param allowedString: Benefits allowed
        :param allowedMoney: Benefits allowed
        :param usedUnsignedInt: Benefits used
        :param usedMoney: Benefits used
        """
        return FhirFinancialBenefit(
            type_=type_,
            allowedUnsignedInt=allowedUnsignedInt,
            allowedString=allowedString,
            allowedMoney=allowedMoney,
            usedUnsignedInt=usedUnsignedInt,
            usedMoney=usedMoney
        )