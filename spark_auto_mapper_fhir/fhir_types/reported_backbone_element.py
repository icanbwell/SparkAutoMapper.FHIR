from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirReportedBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirReportedBackboneElement':
        """
        ReportedBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ReportedBackboneElement
        """
        return FhirReportedBackboneElement(
        )
