from typing import Optional
from pyspark.sql.types import StructType

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta


class $ClassName(FhirResourceBase):
    def __init__(self,
                id_: Optional[FhirId] = None, 
                meta: Optional[Meta] = None,
                extension: Optional[FhirList[Extension]] = None
        ) -> None:
        """
        $ClassName Resource in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        $Documentation
        
        
        :param id_: id of resource
        """
        super().__init__(
            resourceType="$ClassName",
            id_=id_,
            meta=meta,
            extension=extension
            )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ${ClassName}Schema.get_schema(include_extension=include_extension)