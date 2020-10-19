from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.duration import FhirDuration
from spark_auto_mapper_fhir.fhir_types.quantity import FhirQuantity


class FhirFill(FhirResourceBase):
    @classmethod
    def map(
        cls,
        quantity: Optional[FhirQuantity] = None,
        duration: Optional[FhirDuration] = None
    ) -> 'FhirFill':
        """
        Fill Resource in FHIR
        https://hl7.org/FHIR/medicationrequest.html


        :param quantity: fill quantity
        :param duration: fill duration
        """
        return FhirFill(quantity=quantity, duration=duration)
