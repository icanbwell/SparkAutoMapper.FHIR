from typing import Optional

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.identifier import Identifier


class Observation(FhirResourceBase):
    def __init__(
        self, identifier: Optional[FhirList[Identifier]] = None
    ) -> None:
        """
        Observation Resource in FHIR
        http://hl7.org/fhir/observation.html


        :param identifier: Business Identifier for observation
        """
        super().__init__(identifier=identifier)
