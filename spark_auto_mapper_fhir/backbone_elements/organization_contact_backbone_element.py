from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.contactentity_type import ContactEntityTypeCode


class OrganizationContactBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        purpose: Optional[CodeableConcept[ContactEntityTypeCode]] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
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
            id_=id_,
            extension=extension,
            purpose=purpose,
            name=name,
            telecom=telecom,
            address=address,
        )
