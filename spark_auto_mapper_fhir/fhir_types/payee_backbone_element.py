from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_payee_type import ClaimPayeeTypeCode
from spark_auto_mapper_fhir.fhir_types.organization import Organization
from spark_auto_mapper_fhir.fhir_types.patient import Patient
from spark_auto_mapper_fhir.fhir_types.practitioner import Practitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.related_person import RelatedPerson


class PayeeBackboneElement(FhirResourceBase):
    def __init__(
        self,
        type_: Optional[CodeableConcept[ClaimPayeeTypeCode]] = None,
        party: Optional[Reference[Union[Practitioner, PractitionerRole,
                                        Organization, Patient,
                                        RelatedPerson]]] = None
    ):
        """
        PayeeBackboneElement Resource in FHIR
        http://hl7.org/fhir/claim-definitions.html#Claim.payee
        Recipient of benefits payable

        :param type_: Category of recipient https://hl7.org/FHIR/valueset-payeetype.html
        :param party: Recipient reference
        """
        super().__init__(type_=type_, party=party)
