from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirProcedure(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirProcedure':
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        """
        return FhirProcedure(
        )
