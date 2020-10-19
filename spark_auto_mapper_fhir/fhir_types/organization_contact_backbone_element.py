from typing import Optional

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.contact_point import FhirContactPoint
from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.valuesets.contactentity_type import ContactEntityTypeCode


class FhirOrganizationContactBackboneElement(FhirResourceBase):
    def __init__(
        self,
        purpose: Optional[FhirCodeableConcept[ContactEntityTypeCode]] = None,
        name: Optional[FhirHumanName] = None,
        telecom: Optional[FhirList[FhirContactPoint]] = None,
        address: Optional[FhirAddress] = None
    ):
        """
        ContactBackboneElement Resource in FHIR
        http://hl7.org/fhir/organization-definitions.html#Organization.contact
        Contact for the organization for a certain purpose


        :param purpose: The type of contact. http://hl7.org/fhir/valueset-contactentity-type.html
        :param name: A name associated with the contact
        :param telecom: Contact details (telephone, email, etc.) for a contact
        :param address: Visiting or postal addresses for the contact
        """
        super().__init__(
            purpose=purpose, name=name, telecom=telecom, address=address
        )
