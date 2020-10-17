from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FhirSimpleQuantity(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            value: Optional[FhirDecimal] = None,
            unit: Optional[FhirString] = None,
            system: Optional[FhirUri] = None,
            code: Optional[FhirCode] = None
            ) -> 'FhirSimpleQuantity':
        """
        SimpleQuantity Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SimpleQuantity
        The comparator is not used on a SimpleQuantity

        :param value: Numerical value (with implicit precision)
        :param unit: Unit representation
        :param system: System that defines coded unit form
        :param code: Coded form of the unit
        """
        return FhirSimpleQuantity(
            value=value,
            unit=unit,
            system=system,
            code=code
        )
