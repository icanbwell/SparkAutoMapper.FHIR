from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Device(FhirResourceBase):
    def __init__(self) -> None:
        """
        Device Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Device
        """
        super().__init__()
