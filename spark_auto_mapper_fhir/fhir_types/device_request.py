from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirDeviceRequest(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirDeviceRequest':
        """
        DeviceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DeviceRequest
        """
        return FhirDeviceRequest()
