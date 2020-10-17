from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperAmountInputType, AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.uri import AutoMapperFhirUriInputType


class AutoMapperFhirDataTypeDuration(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            value: Optional[AutoMapperAmountInputType] = None,
            comparator: Optional[AutoMapperFhirCodeInputType] = None,
            unit: Optional[AutoMapperTextInputType] = None,
            system: Optional[AutoMapperFhirUriInputType] = None,
            code: Optional[AutoMapperFhirCodeInputType] = None
            ) -> 'AutoMapperFhirDataTypeDuration':
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
        return AutoMapperFhirDataTypeDuration(
            value=value,
            comparator=comparator,
            unit=unit,
            system=system,
            code=code
        )
