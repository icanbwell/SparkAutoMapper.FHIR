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
class MedicationKnowledgeMaxDispense(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        quantity: Quantity,
        period: Optional[Duration] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param quantity: The maximum number of units of the medication that can be dispensed.
        :param period: The period that applies to the maximum number of units.
        """
        super().__init__(
            resourceType="MedicationKnowledgeMaxDispense",
            id_=id_,
            meta=meta,
            extension=extension,
            quantity=quantity,
            period=period,
        )