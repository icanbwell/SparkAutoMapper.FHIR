from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.visionprescription import VisionPrescriptionSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class VisionPrescription(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        VisionPrescription Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#VisionPrescription


        :param id_: id of resource
        """
        super().__init__(
            resourceType="VisionPrescription", id_=id_, meta=meta, extension=extension
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return VisionPrescriptionSchema.get_schema(include_extension=include_extension)
