from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class HealthcareService(FhirResourceBase):
    def __init__(self, id_: Optional[FhirId] = None) -> None:
        """
        HealthcareService Resource in FHIR
        https://hl7.org/FHIR/healthcareservice.html


        :param id_: id of resource
        """
        super().__init__(resourceType="HealthcareService", id_=id_)
