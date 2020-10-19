from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirReportedBackboneElement(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirReportedBackboneElement':
        """
        ReportedBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ReportedBackboneElement
        """
        return FhirReportedBackboneElement()
