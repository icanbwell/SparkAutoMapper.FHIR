from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class ReportedBackboneElement(FhirResourceBase):
    def __init__(self) -> None:
        """
        ReportedBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ReportedBackboneElement
        """
        super().__init__()
