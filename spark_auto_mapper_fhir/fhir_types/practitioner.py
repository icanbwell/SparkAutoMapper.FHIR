from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypePractitioner(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypePractitioner':
        """
        Practitioner Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Practitioner
        """
        return AutoMapperFhirDataTypePractitioner(
        )
