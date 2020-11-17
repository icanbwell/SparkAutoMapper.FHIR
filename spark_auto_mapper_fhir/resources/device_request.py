from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class DeviceRequest(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        DeviceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DeviceRequest


        :param id_: id of resource
        """
        super().__init__(
            resourceType="DeviceRequest", id_=id_, extension=extension
        )
