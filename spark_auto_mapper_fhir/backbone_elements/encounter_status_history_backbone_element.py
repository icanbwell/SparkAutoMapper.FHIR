from typing import Optional

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.encounter_status import EncounterStatusCode


class EncounterStatusHistoryBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        status: EncounterStatusCode,
        period: Period,
    ) -> None:
        """
        EncounterStatushistoryBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/encounter-definitions.html#Encounter.statusHistory
        """
        super().__init__(
            id_=id_,
            status=status,
            period=period,
        )
