from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Endpoint(FhirResourceBase):
    def __init__(self, id_: Optional[FhirId] = None) -> None:
        """
        Endpoint Resource in FHIR
        http://hl7.org/fhir/endpoint.html


        :param id_: id of resource
        """
        super().__init__(resourceType="Endpoint", id_=id_)
