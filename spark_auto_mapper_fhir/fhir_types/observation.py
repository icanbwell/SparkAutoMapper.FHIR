from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirObservation(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirObservation':
        """
        Observation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Observation
        """
        return FhirObservation(
        )
