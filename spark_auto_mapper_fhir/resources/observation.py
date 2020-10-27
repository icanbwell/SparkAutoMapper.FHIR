from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.complex_types.identifier import Identifier


class Observation(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        identifier: Optional[FhirList[Identifier]] = None
    ) -> None:
        """
        Observation Resource in FHIR
        http://hl7.org/fhir/observation.html


        :param id_: id of resource
        :param identifier: Business Identifier for observation
        """
        super().__init__(
            resourceType="Observation", id_=id_, identifier=identifier
        )
