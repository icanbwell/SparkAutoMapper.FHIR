from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class DetectedIssue(FhirResourceBase):
    def __init__(self) -> None:
        """
        DetectedIssue Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DetectedIssue
        """
        super().__init__()
