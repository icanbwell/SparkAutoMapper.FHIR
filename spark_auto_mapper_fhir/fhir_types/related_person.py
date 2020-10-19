from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirRelatedPerson(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirRelatedPerson':
        """
        RelatedPerson Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#RelatedPerson
        """
        return FhirRelatedPerson()
