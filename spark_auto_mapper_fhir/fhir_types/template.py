from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class AutoMapperFhirDataTypeTemplate(FhirResourceBase):
    def __init__(self) -> None:
        """
        Template Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Template
        """
        super().__init__()
