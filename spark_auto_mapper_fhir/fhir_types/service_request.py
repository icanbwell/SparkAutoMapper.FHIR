from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirServiceRequest(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirServiceRequest':
        """
        ServiceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ServiceRequest
        """
        return FhirServiceRequest()
