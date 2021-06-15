from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.immunization_target_disease import (
    ImmunizationTargetDiseaseCode,
)


class ImmunizationProtocolAppliedBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        series: Optional[FhirString] = None,
        authority: Optional[Reference[Organization]] = None,
        targetDisease: Optional[
            FhirList[CodeableConcept[ImmunizationTargetDiseaseCode]]
        ] = None,
        doseNumberPositiveInt: Optional[FhirPositiveInt] = None,
        doseNumberString: Optional[FhirString] = None,
        seriesDosesPositiveInt: Optional[FhirPositiveInt] = None,
        seriesDosesString: Optional[FhirString] = None,
    ) -> None:
        """
        ImmunizationProtocolAppliedBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/immunization-definitions.html#Immunization.protocolApplied
        """
        super().__init__(
            id_=id_,
            series=series,
            authority=authority,
            targetDisease=targetDisease,
            doseNumberPositiveInt=doseNumberPositiveInt,
            doseNumberString=doseNumberString,
            seriesDosesPositiveInt=seriesDosesPositiveInt,
            seriesDosesString=seriesDosesString,
        )
