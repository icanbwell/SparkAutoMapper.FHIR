from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirDevice(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirDevice':
        """
        Device Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Device
        """
        return FhirDevice(
        )
