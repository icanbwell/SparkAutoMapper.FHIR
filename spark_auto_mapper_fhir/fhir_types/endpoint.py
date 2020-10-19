from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirEndpoint(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirEndpoint':
        """
        Endpoint Resource in FHIR
        http://hl7.org/fhir/endpoint.html
        """
        return FhirEndpoint()
