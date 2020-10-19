from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Group(FhirResourceBase):
    def __init__(self) -> None:
        """
        Group Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Group
        """
        super().__init__()
