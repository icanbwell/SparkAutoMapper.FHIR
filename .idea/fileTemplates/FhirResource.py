from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

class Fhir$Name(FhirResourceBase):
    @classmethod
    def map(cls,
            ) -> 'Fhir$Name':
        """
        $Name Resource in FHIR
        $Documentation
        """
        return Fhir$Name(
        )
