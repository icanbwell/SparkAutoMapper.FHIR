from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirProcedure(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirProcedure':
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        """
        return FhirProcedure()
