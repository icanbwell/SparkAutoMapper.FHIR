from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirCarePlan(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirCarePlan':
        """
        CarePlan Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CarePlan
        """
        return FhirCarePlan(
        )
