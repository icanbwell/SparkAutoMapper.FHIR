from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class PractitionerRole(FhirResourceBase):
    def __init__(self) -> None:
        """
        PractitionerRole Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#PractitionerRole
        """
        super().__init__()
