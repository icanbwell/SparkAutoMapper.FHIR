from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirPractitionerRole(FhirResourceBase):
    def __init__(self) -> None:
        """
        PractitionerRole Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#PractitionerRole
        """
        super().__init__()
