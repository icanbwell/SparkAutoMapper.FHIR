from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Procedure(FhirResourceBase):
    def __init__(self) -> None:
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        """
        super().__init__()
