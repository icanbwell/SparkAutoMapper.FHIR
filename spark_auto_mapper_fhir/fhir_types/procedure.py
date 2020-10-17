from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeProcedure(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeProcedure':
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        """
        return AutoMapperFhirDataTypeProcedure(
        )
