from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperAmountInputType

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType


class AutoMapperFhirDataTypeMoney(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            value: Optional[AutoMapperAmountInputType] = None,
            currency: Optional[AutoMapperFhirCodeInputType] = None
            ) -> 'AutoMapperFhirDataTypeMoney':
        """
        Money Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Money
        An amount of economic utility in some recognized currency

        :param value: Numerical value (with implicit precision)
        :param currency: ISO 4217 Currency Code. https://hl7.org/FHIR/valueset-currencies.html
        """
        return AutoMapperFhirDataTypeMoney(
            value=value,
            currency=currency
        )
