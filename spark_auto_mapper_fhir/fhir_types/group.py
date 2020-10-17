from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeGroup(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeGroup':
        """
        Group Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Group
        """
        return AutoMapperFhirDataTypeGroup(
        )
