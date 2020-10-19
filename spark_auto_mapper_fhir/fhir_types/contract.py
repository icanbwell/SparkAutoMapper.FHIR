from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirContract(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirContract':
        """
        Contract Resource in FHIR
        https://hl7.org/FHIR/contract.html
        """
        return FhirContract()
