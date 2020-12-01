from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.device import DeviceSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Device(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Device Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Device


        :param id_: id of resource
        """
        super().__init__(
            resourceType="Device", id_=id_, meta=meta, extension=extension
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return DeviceSchema.get_schema(include_extension=include_extension)
