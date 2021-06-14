from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.valuesets.encounter_location_status import (
    EncounterLocationStatusCode,
)
from spark_auto_mapper_fhir.valuesets.location_type import LocationTypeCode


class EncounterLocationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        location: Reference[Location],
        status: Optional[CodeableConcept[EncounterLocationStatusCode]] = None,
        physicalType: Optional[CodeableConcept[LocationTypeCode]] = None,
        period: Optional[Period] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        EncounterLocationBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/encounter-definitions.html#Encounter.location
        """
        super().__init__(
            id_=id_,
            location=location,
            status=status,
            physicalType=physicalType,
            period=period,
            extension=extension,
        )
