from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirPractitioner(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirPractitioner':
        """
        Practitioner Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Practitioner
        """
        return FhirPractitioner(
        )
