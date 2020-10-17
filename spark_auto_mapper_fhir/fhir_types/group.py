from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirGroup(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirGroup':
        """
        Group Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Group
        """
        return FhirGroup(
        )
