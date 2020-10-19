from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Condition(FhirResourceBase):
    def __init__(self) -> None:
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition
        """
        super().__init__()
