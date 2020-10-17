from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirClaim(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirClaim':
        """
        Claim Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Claim
        """
        return FhirClaim(
        )
