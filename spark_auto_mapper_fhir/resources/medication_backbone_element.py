from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class MedicationBackboneElement(FhirResourceBase):
    def __init__(self) -> None:
        """
        MedicationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#MedicationBackboneElement
        """
        super().__init__()
