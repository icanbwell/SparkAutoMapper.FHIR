from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirClaimResponse(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirClaimResponse':
        """
        ClaimResponse Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ClaimResponse
        """
        return FhirClaimResponse(
        )
