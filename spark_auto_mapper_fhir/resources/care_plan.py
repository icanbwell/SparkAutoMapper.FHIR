from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class CarePlan(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
    ) -> None:
        """
        CarePlan Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CarePlan


        :param id_: id of resource
        """
        super().__init__(resourceType="CarePlan", id_=id_)
