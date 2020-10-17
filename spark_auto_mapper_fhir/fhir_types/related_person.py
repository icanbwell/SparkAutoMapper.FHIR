from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirRelatedPerson(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirRelatedPerson':
        """
        RelatedPerson Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#RelatedPerson
        """
        return FhirRelatedPerson(
        )
