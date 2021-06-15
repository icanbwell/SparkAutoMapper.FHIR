from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.fhir_types.id import FhirId

    from spark_auto_mapper_fhir.resources.observation import Observation


class ImmunizationReactionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        date: Optional[FhirDateTime] = None,
        detail: Optional[Reference[Observation]] = None,
        reported: Optional[FhirBoolean] = None,
    ) -> None:
        """
        ImmunizationReactionBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/immunization-definitions.html#Immunization.reaction
        """
        super().__init__(id_=id_, date=date, detail=detail, reported=reported)
