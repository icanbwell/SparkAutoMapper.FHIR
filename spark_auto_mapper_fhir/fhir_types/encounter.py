from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirEncounter(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirEncounter':
        """
        Encounter Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Encounter
        """
        return FhirEncounter(
        )
