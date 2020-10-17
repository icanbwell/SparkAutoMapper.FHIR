from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirVisionPrescription(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirVisionPrescription':
        """
        VisionPrescription Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#VisionPrescription
        """
        return FhirVisionPrescription(
        )
