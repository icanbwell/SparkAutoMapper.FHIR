from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeTemplate(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeTemplate':
        """
        Template Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Template
        """
        return AutoMapperFhirDataTypeTemplate(
        )
