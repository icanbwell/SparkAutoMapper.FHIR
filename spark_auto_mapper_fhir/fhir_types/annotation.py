from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirAnnotation(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirAnnotation':
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        """
        return FhirAnnotation(
        )
