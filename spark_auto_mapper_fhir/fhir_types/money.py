from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal


class FhirMoney(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            value: Optional[FhirDecimal] = None,
            currency: Optional[FhirCode] = None
            ) -> 'FhirMoney':
        """
        Money Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Money
        An amount of economic utility in some recognized currency

        :param value: Numerical value (with implicit precision)
        :param currency: ISO 4217 Currency Code. https://hl7.org/FHIR/valueset-currencies.html
        """
        return FhirMoney(
            value=value,
            currency=currency
        )
