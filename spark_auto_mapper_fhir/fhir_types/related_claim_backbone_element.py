from typing import Optional

from spark_auto_mapper_fhir.fhir_types.claim import FhirClaim
from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.related_claim_relationship import FhirRelatedClaimRelationshipCode
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirRelatedClaimBackboneElement(FhirResourceBase):
    @classmethod
    def map(
        cls,
        claim: Optional[FhirReference[FhirClaim]] = None,
        # should be FhirClaim but we get circular import
        relationship: Optional[
            FhirCodeableConcept[FhirRelatedClaimRelationshipCode]] = None,
        reference: Optional[FhirIdentifier] = None
    ) -> 'FhirRelatedClaimBackboneElement':
        """
        RelatedClaimBackboneElement Resource in FHIR
        https://hl7.org/FHIR/claim-definitions.html#Claim.related
        Prior or corollary claims

        :param claim: Reference to the related claim
        :param relationship: How the reference claim is related.
                            https://hl7.org/FHIR/valueset-related-claim-relationship.html
        :param reference: 	File or case reference
        """
        return FhirRelatedClaimBackboneElement(
            claim=claim, relationship=relationship, reference=reference
        )
