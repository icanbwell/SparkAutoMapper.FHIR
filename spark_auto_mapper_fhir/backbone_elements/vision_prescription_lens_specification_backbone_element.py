from __future__ import annotations
from typing import Optional

from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity
from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.backbone_elements.vision_prescription_lens_specification_prism_backbone_element import (
    VisionPrescriptionLensSpecificationPrismBackboneElement,
)
from spark_auto_mapper_fhir.valuesets.product import ProductCode
from spark_auto_mapper_fhir.valuesets.vision_eyes import VisionEyesCode


class VisionPrescriptionLensSpecificationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        product: CodeableConcept[ProductCode],
        eye: VisionEyesCode,
        id_: Optional[FhirId] = None,
        sphere: Optional[FhirDecimal] = None,
        cylinder: Optional[FhirDecimal] = None,
        axis: Optional[FhirInteger] = None,
        prism: Optional[
            FhirList[VisionPrescriptionLensSpecificationPrismBackboneElement]
        ] = None,
        add: Optional[FhirDecimal] = None,
        power: Optional[FhirDecimal] = None,
        backCurve: Optional[FhirDecimal] = None,
        diameter: Optional[FhirDecimal] = None,
        duration: Optional[SimpleQuantity] = None,
        color: Optional[FhirString] = None,
        brand: Optional[FhirString] = None,
        note: Optional[FhirList[Annotation]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        LensSpecification Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
        properties not just the ones you need
        https://hl7.org/FHIR/visionprescription-definitions.html#VisionPrescription.lensSpecification
        """
        super().__init__(
            id_=id_,
            extension=extension,
            product=product,
            eye=eye,
            sphere=sphere,
            cylinder=cylinder,
            axis=axis,
            prism=prism,
            add=add,
            power=power,
            backCurve=backCurve,
            diameter=diameter,
            duration=duration,
            color=color,
            brand=brand,
            note=note,
        )
