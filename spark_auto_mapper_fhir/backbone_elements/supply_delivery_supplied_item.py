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
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # itemCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for itemCodeableConcept
    # Import for CodeableConcept for itemCodeableConcept
    from spark_auto_mapper_fhir.value_sets.snomedct_supply_item import (
        SNOMEDCTSupplyItemCode,
    )

    # End Import for CodeableConcept for itemCodeableConcept
    # itemReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for itemReference
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance
    from spark_auto_mapper_fhir.resources.device import Device


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SupplyDeliverySuppliedItem(FhirBackboneElementBase):
    """
    SupplyDelivery.SuppliedItem
        Record of delivery of what is supplied.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        quantity: Optional[Quantity] = None,
        itemCodeableConcept: Optional[CodeableConcept[SNOMEDCTSupplyItemCode]] = None,
        itemReference: Optional[Reference[Union[Medication, Substance, Device]]] = None,
    ) -> None:
        """
            Record of delivery of what is supplied.

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
            :param quantity: The amount of supply that has been dispensed. Includes unit of measure.
            :param itemCodeableConcept: None
            :param itemReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            quantity=quantity,
            itemCodeableConcept=itemCodeableConcept,
            itemReference=itemReference,
        )
