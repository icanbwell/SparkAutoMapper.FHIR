from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirCarePlan(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirCarePlan':
        """
        CarePlan Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CarePlan
        """
        return FhirCarePlan()
