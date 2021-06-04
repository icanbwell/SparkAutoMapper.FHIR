from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class EligibilityBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[FhirValueSetBase]] = None,
        comment: Optional[FhirMarkdown] = None,
    ) -> None:
        """
        EligibilityBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/healthcareservice-definitions.html#HealthcareService.eligibility
        Specific eligibility requirements required to use the service

        :param code: Coded value for the eligibility
        :param comment: Describes the eligibility conditions for the service
        """
        super().__init__(id_=id_, extension=extension, code=code, comment=comment)
