from typing import Optional, Union

from spark_auto_mapper_fhir.resources.clinical_impression import ClinicalImpression
from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
from spark_auto_mapper_fhir.resources.observation import Observation

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.condition_stage import ConditionStageCode
from spark_auto_mapper_fhir.valuesets.condition_stage_type import ConditionStageTypeCode


class ConditionStageBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        summary: Optional[CodeableConcept[ConditionStageCode]] = None,
        assessment: Optional[FhirList[Reference[Union[ClinicalImpression,
                                                      DiagnosticReport,
                                                      Observation]]]] = None,
        type_: Optional[CodeableConcept[ConditionStageTypeCode]] = None
    ) -> None:
        """
        ConditionStageBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/condition-definitions.html#Condition.stage
        Clinical stage or grade of a condition. May include formal severity assessments.


        :param summary: A simple summary of the stage such as "Stage 3". The determination of the stage is disease-specific.
        :param assessment: Reference to a formal record of the evidence on which the staging assessment is based.
        :param type_: The kind of staging, such as pathological or clinical staging.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            summary=summary,
            assessment=assessment,
            type_=type_
        )
