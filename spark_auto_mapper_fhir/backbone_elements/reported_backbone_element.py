from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase


class ReportedBackboneElement(FhirBackboneElementBase):
    def __init__(self) -> None:
        """
        ReportedBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ReportedBackboneElement
        """
        super().__init__()
