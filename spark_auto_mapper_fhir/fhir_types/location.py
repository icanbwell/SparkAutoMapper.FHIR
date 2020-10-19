from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirLocation(FhirResourceBase):
    def __init__(
        self,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        name: Optional[FhirString] = None
    ):
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location


        """
        super().__init__(identifier=identifier, name=name)
