from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.observation import ObservationSchema

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.complex_types.identifier import Identifier


class Observation(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        identifier: Optional[FhirList[Identifier]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Observation Resource in FHIR
        http://hl7.org/fhir/observation.html


        :param id_: id of resource
        :param identifier: Business Identifier for observation
        """
        super().__init__(
            resourceType="Observation",
            id_=id_,
            identifier=identifier,
            extension=extension
        )

    def get_schema(self) -> Optional[StructType]:
        return ObservationSchema.get_schema()
