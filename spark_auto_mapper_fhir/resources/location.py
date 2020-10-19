from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Location(FhirResourceBase):
    def __init__(
        self,
        identifier: Optional[FhirList[Identifier]] = None,
        name: Optional[FhirString] = None
    ):
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location


        """
        super().__init__(identifier=identifier, name=name)
