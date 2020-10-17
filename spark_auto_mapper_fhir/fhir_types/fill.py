from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.duration import AutoMapperFhirDataTypeDuration
from spark_auto_mapper_fhir.fhir_types.quantity import AutoMapperFhirDataTypeQuantity


class AutoMapperFhirDataTypeFill(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            quantity: Optional[AutoMapperFhirDataTypeQuantity] = None,
            duration: Optional[AutoMapperFhirDataTypeDuration] = None
            ) -> 'AutoMapperFhirDataTypeFill':
        """
        Fill Resource in FHIR
        https://hl7.org/FHIR/medicationrequest.html


        :param quantity: fill quantity
        :param duration: fill duration
        """
        return AutoMapperFhirDataTypeFill(
            quantity=quantity,
            duration=duration
        )
