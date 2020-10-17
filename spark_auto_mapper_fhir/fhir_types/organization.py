from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirOrganization(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirOrganization':
        """
        Organization Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Organization
        """
        return FhirOrganization(
        )
