from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirAnnotation(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirAnnotation':
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        """
        return FhirAnnotation()
