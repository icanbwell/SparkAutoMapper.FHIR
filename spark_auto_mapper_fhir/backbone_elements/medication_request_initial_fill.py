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
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationRequestInitialFill(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        quantity: Optional[Quantity] = None,
        duration: Optional[Duration] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param quantity: The amount or quantity to provide as part of the first dispense.
        :param duration: The length of time that the first dispense is expected to last.
        """
        super().__init__(
            resourceType="MedicationRequestInitialFill",
            id_=id_,
            meta=meta,
            extension=extension,
            quantity=quantity,
            duration=duration,
        )