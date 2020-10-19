from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirLocation(FhirResourceBase):
    @classmethod
    def map(
        cls,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        name: Optional[FhirString] = None
    ) -> 'FhirLocation':
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location


        """
        return FhirLocation(identifier=identifier, name=name)
