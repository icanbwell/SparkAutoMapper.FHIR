from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.codes.related_claim_relationship import FhirRelatedClaimRelationshipCode
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirRelatedClaimBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            claim: Optional[FhirReference[AutoMapperDataTypeComplexBase]] = None,
            # should be FhirClaim but we get circular import
            relationship: Optional[FhirCodeableConcept[FhirRelatedClaimRelationshipCode]] = None,
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
            claim=claim,
            relationship=relationship,
            reference=reference
        )
