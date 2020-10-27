from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.resources.claim import Claim

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.related_claim_relationship import RelatedClaimRelationshipCode
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference


class RelatedClaimBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        claim: Optional[Reference[Claim]] = None,
        # should be FhirClaim but we get circular import
        relationship: Optional[CodeableConcept[RelatedClaimRelationshipCode]
                               ] = None,
        reference: Optional[Identifier] = None
    ):
        """
        RelatedClaimBackboneElement Resource in FHIR
        https://hl7.org/FHIR/claim-definitions.html#Claim.related
        Prior or corollary claims

        :param claim: Reference to the related claim
        :param relationship: How the reference claim is related.
                            https://hl7.org/FHIR/valueset-related-claim-relationship.html
        :param reference: 	File or case reference
        """
        super().__init__(
            claim=claim, relationship=relationship, reference=reference
        )
