from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device_definition import DeviceDefinition
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manufacturedItem
    from spark_auto_mapper_fhir.resources.medicinal_product_manufactured import (
        MedicinalProductManufactured,
    )
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_packaged_package_item import (
        MedicinalProductPackagedPackageItem,
    )
    from spark_auto_mapper_fhir.backbone_elements.prod_characteristic import (
        ProdCharacteristic,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.backbone_elements.product_shelf_life import (
        ProductShelfLife,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductPackagedPackageItem(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        type: CodeableConcept,
        quantity: Quantity,
        material: Optional[FhirList[CodeableConcept]] = None,
        alternateMaterial: Optional[FhirList[CodeableConcept]] = None,
        device: Optional[FhirList[Reference[Union[DeviceDefinition]]]] = None,
        manufacturedItem: Optional[
            FhirList[Reference[Union[MedicinalProductManufactured]]]
        ] = None,
        packageItem: Optional[FhirList[MedicinalProductPackagedPackageItem]] = None,
        physicalCharacteristics: Optional[ProdCharacteristic] = None,
        otherCharacteristics: Optional[FhirList[CodeableConcept]] = None,
        shelfLifeStorage: Optional[FhirList[ProductShelfLife]] = None,
        manufacturer: Optional[FhirList[Reference[Union[Organization]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Including possibly Data Carrier Identifier.
            :param type: The physical type of the container of the medicine.
            :param quantity: The quantity of this package in the medicinal product, at the current level of
        packaging. The outermost is always 1.
            :param material: Material type of the package item.
            :param alternateMaterial: A possible alternate material for the packaging.
            :param device: A device accompanying a medicinal product.
            :param manufacturedItem: The manufactured item as contained in the packaged medicinal product.
            :param packageItem: Allows containers within containers.
            :param physicalCharacteristics: Dimensions, color etc.
            :param otherCharacteristics: Other codeable characteristics.
            :param shelfLifeStorage: Shelf Life and storage information.
            :param manufacturer: Manufacturer of this Package Item.
        """
        super().__init__(
            resourceType="MedicinalProductPackagedPackageItem",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            type=type,
            quantity=quantity,
            material=material,
            alternateMaterial=alternateMaterial,
            device=device,
            manufacturedItem=manufacturedItem,
            packageItem=packageItem,
            physicalCharacteristics=physicalCharacteristics,
            otherCharacteristics=otherCharacteristics,
            shelfLifeStorage=shelfLifeStorage,
            manufacturer=manufacturer,
        )