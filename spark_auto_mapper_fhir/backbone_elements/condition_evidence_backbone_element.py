from typing import Optional, Any

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.manifestation_or_symptom import (
    ManifestationAndSymptomCode,
)


class ConditionEvidenceBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[FhirList[CodeableConcept[ManifestationAndSymptomCode]]] = None,
        detail: Optional[FhirList[Any]] = None,
    ) -> None:
        """
        ConditionEvidenceBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/condition-definitions.html#Condition.evidence
        Supporting evidence
        + Rule: evidence SHALL have code or details


        :param code: Manifestation/symptom
        :param detail: Supporting information found elsewhere
        """
        super().__init__(id_=id_, extension=extension, code=code, detail=detail)
