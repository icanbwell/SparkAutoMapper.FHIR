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
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manipulated
    from spark_auto_mapper_fhir.resources.device import Device


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProcedureFocalDevice(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        action: Optional[CodeableConcept] = None,
        manipulated: Reference[Union[Device]],
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param action: The kind of change that happened to the device during the procedure.
        :param manipulated: The device that was manipulated (changed) during the procedure.
        """
        super().__init__(
            resourceType="ProcedureFocalDevice",
            id_=id_,
            meta=meta,
            extension=extension,
            action=action,
            manipulated=manipulated,
        )