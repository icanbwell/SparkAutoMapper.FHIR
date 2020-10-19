from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class CareTeam(FhirResourceBase):
    def __init__(self) -> None:
        """
        CareTeam Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CareTeam
        """
        super().__init__()
