from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # purpose (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for purpose
    # Import for CodeableConcept for purpose
    from spark_auto_mapper_fhir.value_sets.contact_entity_type import (
        ContactEntityTypeCode,
    )

    # End Import for CodeableConcept for purpose
    # name (HumanName)
    from spark_auto_mapper_fhir.complex_types.human_name import HumanName

    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # address (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InsurancePlanContact(FhirBackboneElementBase):
    """
    InsurancePlan.Contact
        Details of a Health Insurance product/plan provided by an organization.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        purpose: Optional[CodeableConcept[ContactEntityTypeCode]] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
    ) -> None:
        """
            Details of a Health Insurance product/plan provided by an organization.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param purpose: Indicates a purpose for which the contact can be reached.
            :param name: A name associated with the contact.
            :param telecom: A contact detail (e.g. a telephone number or an email address) by which the
        party may be contacted.
            :param address: Visiting or postal addresses for the contact.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            purpose=purpose,
            name=name,
            telecom=telecom,
            address=address,
        )
