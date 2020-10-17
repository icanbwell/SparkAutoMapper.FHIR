from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirDetectedIssue(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirDetectedIssue':
        """
        DetectedIssue Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DetectedIssue
        """
        return FhirDetectedIssue(
        )
