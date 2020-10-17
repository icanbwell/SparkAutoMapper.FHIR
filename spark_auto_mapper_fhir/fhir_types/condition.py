from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeCondition(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeCondition':
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition
        """
        return AutoMapperFhirDataTypeCondition(
        )
