from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirCareTeam(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirCareTeam':
        """
        CareTeam Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CareTeam
        """
        return FhirCareTeam()
