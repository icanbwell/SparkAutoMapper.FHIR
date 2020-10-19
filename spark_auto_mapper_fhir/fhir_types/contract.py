from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirContract(FhirResourceBase):
    def __init__(self) -> None:
        """
        Contract Resource in FHIR
        https://hl7.org/FHIR/contract.html
        """
        super().__init__()
