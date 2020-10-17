from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeDevice(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeDevice':
        """
        Device Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Device
        """
        return AutoMapperFhirDataTypeDevice(
        )
