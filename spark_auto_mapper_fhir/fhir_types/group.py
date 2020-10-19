from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirGroup(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirGroup':
        """
        Group Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Group
        """
        return FhirGroup()
