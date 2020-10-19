from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class ServiceRequest(FhirResourceBase):
    def __init__(self) -> None:
        """
        ServiceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ServiceRequest
        """
        super().__init__()
