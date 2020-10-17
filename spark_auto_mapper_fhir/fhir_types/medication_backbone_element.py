from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeMedicationBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeMedicationBackboneElement':
        """
        MedicationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#MedicationBackboneElement
        """
        return AutoMapperFhirDataTypeMedicationBackboneElement(
        )
