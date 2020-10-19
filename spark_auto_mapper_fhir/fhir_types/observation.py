from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirObservation(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirObservation':
        """
        Observation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Observation
        """
        return FhirObservation()
