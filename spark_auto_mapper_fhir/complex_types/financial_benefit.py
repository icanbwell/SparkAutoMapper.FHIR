from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.benefit_type import BenefitTypeCode
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


class FinancialBenefit(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[CodeableConcept[BenefitTypeCode]] = None,
        allowedUnsignedInt: Optional[FhirUnsignedInt] = None,
        allowedString: Optional[FhirString] = None,
        allowedMoney: Optional[Money] = None,
        usedUnsignedInt: Optional[FhirUnsignedInt] = None,
        usedMoney: Optional[Money] = None,
    ):
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
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            allowedUnsignedInt=allowedUnsignedInt,
            allowedString=allowedString,
            allowedMoney=allowedMoney,
            usedUnsignedInt=usedUnsignedInt,
            usedMoney=usedMoney,
        )
