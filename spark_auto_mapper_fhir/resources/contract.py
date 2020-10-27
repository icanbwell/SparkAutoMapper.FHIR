from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Contract(FhirResourceBase):
    def __init__(self, id_: Optional[FhirId] = None) -> None:
        """
        Contract Resource in FHIR
        https://hl7.org/FHIR/contract.html


        :param id_: id of resource
        """
        super().__init__(resourceType="Contract", id_=id_)
