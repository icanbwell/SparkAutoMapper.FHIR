from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Annotation(FhirResourceBase):
    def __init__(self) -> None:
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        """
        super().__init__()
