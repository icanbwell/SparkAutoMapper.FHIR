from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Location(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        name: Optional[FhirString] = None
    ):
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location



        :param id_: id of resource
        """
        super().__init__(
            resourceType="Location", id_=id_, identifier=identifier, name=name
        )
