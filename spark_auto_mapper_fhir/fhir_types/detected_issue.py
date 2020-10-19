from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirDetectedIssue(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirDetectedIssue':
        """
        DetectedIssue Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DetectedIssue
        """
        return FhirDetectedIssue()
