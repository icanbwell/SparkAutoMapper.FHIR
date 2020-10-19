from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirClaimResponse(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirClaimResponse':
        """
        ClaimResponse Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ClaimResponse
        """
        return FhirClaimResponse()
