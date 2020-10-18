from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class Fhir$Name(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'Fhir$Name':
        """
        $Name Resource in FHIR
        $Documentation
        """
        return Fhir$Name(
        )
