from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.integer import integer
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.backbone_elements.substance_polymer_repeat_unit import (
        SubstancePolymerRepeatUnit,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstancePolymerRepeat(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        numberOfUnits: Optional[integer] = None,
        averageMolecularFormula: Optional[string] = None,
        repeatUnitAmountType: Optional[CodeableConcept] = None,
        repeatUnit: Optional[FhirList[SubstancePolymerRepeatUnit]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param numberOfUnits: Todo.
        :param averageMolecularFormula: Todo.
        :param repeatUnitAmountType: Todo.
        :param repeatUnit: Todo.
        """
        super().__init__(
            resourceType="SubstancePolymerRepeat",
            id_=id_,
            meta=meta,
            extension=extension,
            numberOfUnits=numberOfUnits,
            averageMolecularFormula=averageMolecularFormula,
            repeatUnitAmountType=repeatUnitAmountType,
            repeatUnit=repeatUnit,
        )