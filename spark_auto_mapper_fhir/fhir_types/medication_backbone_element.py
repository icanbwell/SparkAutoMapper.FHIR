from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirMedicationBackboneElement(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirMedicationBackboneElement':
        """
        MedicationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#MedicationBackboneElement
        """
        return FhirMedicationBackboneElement()
