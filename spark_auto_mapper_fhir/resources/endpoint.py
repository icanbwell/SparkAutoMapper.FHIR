from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.endpoint import EndpointSchema

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Endpoint(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Endpoint Resource in FHIR
        http://hl7.org/fhir/endpoint.html


        :param id_: id of resource
        """
        super().__init__(resourceType="Endpoint", id_=id_, extension=extension)

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return EndpointSchema.get_schema(include_extension=include_extension)
