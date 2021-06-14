from typing import Optional, Union, TYPE_CHECKING

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.valuesets.encounter_diagnosis_role import (
    EncounterDiagnosisRoleCode,
)


class EncounterDiagnosisBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        condition: Reference[Union["Condition", Procedure]],
        use: Optional[CodeableConcept[EncounterDiagnosisRoleCode]] = None,
        rank: Optional[FhirPositiveInt] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        EncounterDiagnosisBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/encounter-definitions.html#Encounter.diagnosis Added
        """
        super().__init__(
            id_=id_, condition=condition, use=use, rank=rank, extension=extension
        )
