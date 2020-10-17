from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FhirDuration(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            value: Optional[FhirDecimal] = None,
            comparator: Optional[FhirCode] = None,
            unit: Optional[FhirString] = None,
            system: Optional[FhirUri] = None,
            code: Optional[FhirCode] = None
            ) -> 'FhirDuration':
        """
        Duration Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Duration


        :param value: Numerical value (with implicit precision)
        :param comparator: < | <= | >= | > - how to understand the value.
                            https://hl7.org/FHIR/valueset-Duration-comparator.html
        :param unit: Unit representation
        :param system: System that defines coded unit form
        :param code: Coded form of the unit
        """
        return FhirDuration(
            value=value,
            comparator=comparator,
            unit=unit,
            system=system,
            code=code
        )
