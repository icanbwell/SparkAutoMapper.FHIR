from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirImmunizationRecommendation(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirImmunizationRecommendation':
        """
        ImmunizationRecommendation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ImmunizationRecommendation
        """
        return FhirImmunizationRecommendation()
