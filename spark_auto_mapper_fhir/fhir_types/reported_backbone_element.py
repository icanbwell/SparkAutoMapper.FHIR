from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeReportedBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'AutoMapperFhirDataTypeReportedBackboneElement':
        """
        ReportedBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ReportedBackboneElement
        """
        return AutoMapperFhirDataTypeReportedBackboneElement(
        )
