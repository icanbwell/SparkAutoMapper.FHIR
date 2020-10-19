from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class AutoMapperFhirDataTypeTemplate(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'AutoMapperFhirDataTypeTemplate':
        """
        Template Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Template
        """
        return AutoMapperFhirDataTypeTemplate()
