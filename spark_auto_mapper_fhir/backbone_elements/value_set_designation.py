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
    from spark_auto_mapper_fhir.complex_types.code import code
    from spark_auto_mapper_fhir.complex_types.coding import Coding
    from spark_auto_mapper_fhir.complex_types.string import string


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetDesignation(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        language: Optional[code] = None,
        use: Optional[Coding] = None,
        value: string,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param language: The language this designation is defined for.
        :param use: A code that represents types of uses of designations.
        :param value: The text value for this designation.
        """
        super().__init__(
            resourceType="ValueSetDesignation",
            id_=id_,
            meta=meta,
            extension=extension,
            language=language,
            use=use,
            value=value,
        )