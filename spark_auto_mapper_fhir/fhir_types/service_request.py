from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirServiceRequest(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirServiceRequest':
        """
        ServiceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ServiceRequest
        """
        return FhirServiceRequest(
        )
