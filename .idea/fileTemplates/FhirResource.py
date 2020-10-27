from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

class $ClassName(FhirResourceBase):
    def __init__(self,id_: Optional[FhirId] = None) -> None:
        """
        $ClassName Resource in FHIR
        $Documentation
        """
        super().__init__(
            resourceType="$ClassName",
            id_=id_
            )
