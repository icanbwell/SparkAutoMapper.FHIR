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
    from spark_auto_mapper_fhir.complex_types.date import date
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.backbone_elements.value_set_include import (
        ValueSetInclude,
    )
    from spark_auto_mapper_fhir.backbone_elements.value_set_include import (
        ValueSetInclude,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetCompose(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        lockedDate: Optional[date] = None,
        inactive: Optional[boolean] = None,
        include: FhirList[ValueSetInclude],
        exclude: Optional[FhirList[ValueSetInclude]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param lockedDate: The Locked Date is  the effective date that is used to determine the version
        of all referenced Code Systems and Value Set Definitions included in the
        compose that are not already tied to a specific version.
            :param inactive: Whether inactive codes - codes that are not approved for current use - are in
        the value set. If inactive = true, inactive codes are to be included in the
        expansion, if inactive = false, the inactive codes will not be included in the
        expansion. If absent, the behavior is determined by the implementation, or by
        the applicable $expand parameters (but generally, inactive codes would be
        expected to be included).
            :param include: Include one or more codes from a code system or other value set(s).
            :param exclude: Exclude one or more codes from the value set based on code system filters
        and/or other value sets.
        """
        super().__init__(
            resourceType="ValueSetCompose",
            id_=id_,
            meta=meta,
            extension=extension,
            lockedDate=lockedDate,
            inactive=inactive,
            include=include,
            exclude=exclude,
        )