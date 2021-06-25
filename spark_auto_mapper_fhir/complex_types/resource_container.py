from __future__ import annotations

from typing import Optional, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId


class ResourceContainer(FhirResourceBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
    ) -> None:
        """
        Resource Resource in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need



        :param id_: id of resource
        """
        super().__init__(
            resourceType="Resource",
            id_=id_,
            meta=meta,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return None
