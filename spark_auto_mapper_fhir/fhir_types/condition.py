from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirCondition(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirCondition':
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition
        """
        return FhirCondition(
        )
