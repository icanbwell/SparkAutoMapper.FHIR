from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeOrganization(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeOrganization':
        """
        Organization Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Organization
        """
        return AutoMapperFhirDataTypeOrganization(
        )
