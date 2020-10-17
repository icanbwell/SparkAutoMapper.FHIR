from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypePractitionerRole(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypePractitionerRole':
        """
        PractitionerRole Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#PractitionerRole
        """
        return AutoMapperFhirDataTypePractitionerRole(
        )
