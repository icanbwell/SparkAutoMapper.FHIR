from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirMedicationBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirMedicationBackboneElement':
        """
        MedicationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#MedicationBackboneElement
        """
        return FhirMedicationBackboneElement(
        )
