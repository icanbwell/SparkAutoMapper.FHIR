from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeEncounter(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeEncounter':
        """
        Encounter Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Encounter
        """
        return AutoMapperFhirDataTypeEncounter(
        )
