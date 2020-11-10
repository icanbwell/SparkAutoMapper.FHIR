from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension


class $ClassName(FhirResourceBase):
    def __init__(self,
                id_: Optional[FhirId] = None, 
                extension: Optional[FhirList[Extension]] = None
        ) -> None:
        """
        $ClassName Resource in FHIR
        $Documentation
        
        
        :param id_: id of resource
        """
        super().__init__(
            resourceType="$ClassName",
            id_=id_,
            extension=extension
            )
