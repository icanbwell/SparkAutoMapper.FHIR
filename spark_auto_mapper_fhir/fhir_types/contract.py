from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirContract(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirContract':
        """
        Contract Resource in FHIR
        https://hl7.org/FHIR/contract.html
        """
        return FhirContract(
        )
