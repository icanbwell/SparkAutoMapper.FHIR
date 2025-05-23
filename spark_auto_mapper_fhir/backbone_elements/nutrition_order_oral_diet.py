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
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.diet_codes import DietCodesCode

    # End Import for CodeableConcept for type_
    # schedule (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # nutrient (NutritionOrder.Nutrient)
    from spark_auto_mapper_fhir.backbone_elements.nutrition_order_nutrient import (
        NutritionOrderNutrient,
    )

    # texture (NutritionOrder.Texture)
    from spark_auto_mapper_fhir.backbone_elements.nutrition_order_texture import (
        NutritionOrderTexture,
    )

    # fluidConsistencyType (CodeableConcept)
    # End Import for References for fluidConsistencyType
    # Import for CodeableConcept for fluidConsistencyType
    from spark_auto_mapper_fhir.value_sets.fluid_consistency_type_codes import (
        FluidConsistencyTypeCodesCode,
    )

    # End Import for CodeableConcept for fluidConsistencyType
    # instruction (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NutritionOrderOralDiet(FhirBackboneElementBase):
    """
    NutritionOrder.OralDiet
        A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[FhirList[CodeableConcept[DietCodesCode]]] = None,
        schedule: Optional[FhirList[Timing]] = None,
        nutrient: Optional[FhirList[NutritionOrderNutrient]] = None,
        texture: Optional[FhirList[NutritionOrderTexture]] = None,
        fluidConsistencyType: Optional[
            FhirList[CodeableConcept[FluidConsistencyTypeCodesCode]]
        ] = None,
        instruction: Optional[FhirString] = None,
    ) -> None:
        """
            A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.

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
            :param type_: The kind of diet or dietary restriction such as fiber restricted diet or
        diabetic diet.
            :param schedule: The time period and frequency at which the diet should be given.  The diet
        should be given for the combination of all schedules if more than one schedule
        is present.
            :param nutrient: Class that defines the quantity and type of nutrient modifications (for
        example carbohydrate, fiber or sodium) required for the oral diet.
            :param texture: Class that describes any texture modifications required for the patient to
        safely consume various types of solid foods.
            :param fluidConsistencyType: The required consistency (e.g. honey-thick, nectar-thick, thin, thickened.) of
        liquids or fluids served to the patient.
            :param instruction: Free text or additional instructions or information pertaining to the oral
        diet.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            schedule=schedule,
            nutrient=nutrient,
            texture=texture,
            fluidConsistencyType=fluidConsistencyType,
            instruction=instruction,
        )
