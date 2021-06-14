from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.valuesets.diagnosis_role import DiagnosisRole


class EpisodeOfCareDiagnosisBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        condition: Reference[Condition],
        role: Optional[CodeableConcept[DiagnosisRole]] = None,
        rank: Optional[FhirPositiveInt] = None,
    ) -> None:
        """
        EpisodeOfCareDiagnosis Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/episodeofcare-definitions.html#EpisodeOfCare.diagnosis
        """
        super().__init__(
            id_=id_,
            condition=condition,
            role=role,
            rank=rank,
        )
