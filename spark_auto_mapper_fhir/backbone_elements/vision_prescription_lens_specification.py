from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
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
    # product (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for product
    # Import for CodeableConcept for product
    from spark_auto_mapper_fhir.value_sets.example_vision_prescription_product_codes import (
        ExampleVisionPrescriptionProductCodesCode,
    )

    # End Import for CodeableConcept for product
    # eye (VisionEyes)
    from spark_auto_mapper_fhir.value_sets.vision_eyes import VisionEyesCode

    # sphere (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # cylinder (decimal)
    # axis (integer)
    # prism (VisionPrescription.Prism)
    from spark_auto_mapper_fhir.backbone_elements.vision_prescription_prism import (
        VisionPrescriptionPrism,
    )

    # add (decimal)
    # power (decimal)
    # backCurve (decimal)
    # diameter (decimal)
    # duration (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # color (string)
    # brand (string)
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class VisionPrescriptionLensSpecification(FhirBackboneElementBase):
    """
    VisionPrescription.LensSpecification
        An authorization for the provision of glasses and/or contact lenses to a patient.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        product: CodeableConcept[ExampleVisionPrescriptionProductCodesCode],
        eye: VisionEyesCode,
        sphere: Optional[FhirDecimal] = None,
        cylinder: Optional[FhirDecimal] = None,
        axis: Optional[FhirInteger] = None,
        prism: Optional[FhirList[VisionPrescriptionPrism]] = None,
        add: Optional[FhirDecimal] = None,
        power: Optional[FhirDecimal] = None,
        backCurve: Optional[FhirDecimal] = None,
        diameter: Optional[FhirDecimal] = None,
        duration: Optional[Quantity] = None,
        color: Optional[FhirString] = None,
        brand: Optional[FhirString] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
            An authorization for the provision of glasses and/or contact lenses to a
        patient.

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
            :param product: Identifies the type of vision correction product which is required for the
        patient.
            :param eye: The eye for which the lens specification applies.
            :param sphere: Lens power measured in dioptres (0.25 units).
            :param cylinder: Power adjustment for astigmatism measured in dioptres (0.25 units).
            :param axis: Adjustment for astigmatism measured in integer degrees.
            :param prism: Allows for adjustment on two axis.
            :param add: Power adjustment for multifocal lenses measured in dioptres (0.25 units).
            :param power: Contact lens power measured in dioptres (0.25 units).
            :param backCurve: Back curvature measured in millimetres.
            :param diameter: Contact lens diameter measured in millimetres.
            :param duration: The recommended maximum wear period for the lens.
            :param color: Special color or pattern.
            :param brand: Brand recommendations or restrictions.
            :param note: Notes for special requirements such as coatings and lens materials.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
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
