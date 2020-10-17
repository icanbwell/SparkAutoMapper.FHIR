from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirCareTeam(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirCareTeam':
        """
        CareTeam Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CareTeam
        """
        return FhirCareTeam(
        )
