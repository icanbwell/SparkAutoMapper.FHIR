from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class DeviceRequest(FhirResourceBase):
    def __init__(self, ) -> None:
        """
        DeviceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DeviceRequest
        """
        super().__init__()
