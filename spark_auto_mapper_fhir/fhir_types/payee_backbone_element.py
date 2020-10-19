from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_payee_type import FhirClaimPayeeTypeCode
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_person import FhirRelatedPerson


class FhirPayeeBackboneElement(FhirResourceBase):
    @classmethod
    def map(
        cls,
        type_: Optional[FhirCodeableConcept[FhirClaimPayeeTypeCode]] = None,
        party: Optional[FhirReference[Union[FhirPractitioner,
                                            FhirPractitionerRole,
                                            FhirOrganization, FhirPatient,
                                            FhirRelatedPerson]]] = None
    ) -> 'FhirPayeeBackboneElement':
        """
        PayeeBackboneElement Resource in FHIR
        http://hl7.org/fhir/claim-definitions.html#Claim.payee
        Recipient of benefits payable

        :param type_: Category of recipient https://hl7.org/FHIR/valueset-payeetype.html
        :param party: Recipient reference
        """
        return FhirPayeeBackboneElement(type_=type_, party=party)
