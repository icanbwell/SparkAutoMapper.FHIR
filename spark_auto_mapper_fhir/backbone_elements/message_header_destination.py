from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # name (string)
    # target (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for target
    from spark_auto_mapper_fhir.resources.device import Device

    # endpoint (url)
    from spark_auto_mapper_fhir.fhir_types.url import FhirUrl

    # receiver (Reference)
    # Imports for References for receiver
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MessageHeaderDestination(FhirBackboneElementBase):
    """
    MessageHeader.Destination
        The header for a message exchange that is either requesting or responding to an action.  The reference(s) that are the subject of the action as well as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        name: Optional[FhirString] = None,
        target: Optional[Reference[Device]] = None,
        endpoint: FhirUrl,
        receiver: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
    ) -> None:
        """
            The header for a message exchange that is either requesting or responding to
        an action.  The reference(s) that are the subject of the action as well as
        other information related to the action are typically transmitted in a bundle
        in which the MessageHeader resource instance is the first resource in the
        bundle.

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
            :param name: Human-readable name for the target system.
            :param target: Identifies the target end system in situations where the initial message
        transmission is to an intermediary system.
            :param endpoint: Indicates where the message should be routed to.
            :param receiver: Allows data conveyed by a message to be addressed to a particular person or
        department when routing to a specific application isn't sufficient.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            name=name,
            target=target,
            endpoint=endpoint,
            receiver=receiver,
        )
