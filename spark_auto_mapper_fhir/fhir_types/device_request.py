from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirDeviceRequest(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirDeviceRequest':
        """
        DeviceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DeviceRequest
        """
        return FhirDeviceRequest(
        )
