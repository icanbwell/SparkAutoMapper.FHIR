from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class CarePlan(FhirResourceBase):
    def __init__(self) -> None:
        """
        CarePlan Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CarePlan
        """
        super().__init__()
