from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.resources.claim import Claim

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.claim_relationship import ClaimRelationshipCode


class ExplanationOfBenefitRelatedBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        claim: Optional[Reference[Claim]] = None,
        relationship: Optional[CodeableConcept[ClaimRelationshipCode]] = None,
        reference: Optional[FhirId] = None
    ) -> None:
        """
        ExplanationOfBenefitRelatedBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.related
        Prior or corollary claims


        :param claim: Reference to the related claim
        :param relationship: How the reference claim is related
        :param reference: File or case reference
        """
        super().__init__(
            id_=id_,
            extension=extension,
            claim=claim,
            relationship=relationship,
            reference=reference
        )
