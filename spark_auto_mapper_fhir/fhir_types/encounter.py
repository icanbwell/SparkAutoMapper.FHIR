from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirEncounter(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirEncounter':
        """
        Encounter Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Encounter
        """
        return FhirEncounter()
