from typing import Optional

from spark_auto_mapper_fhir.resources.address import Address
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.resources.contact_point import ContactPoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.contactentity_type import ContactEntityTypeCode


class OrganizationContactBackboneElement(FhirResourceBase):
    def __init__(
        self,
        purpose: Optional[CodeableConcept[ContactEntityTypeCode]] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None
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
