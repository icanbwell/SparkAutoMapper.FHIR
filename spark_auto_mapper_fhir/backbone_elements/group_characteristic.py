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
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GroupCharacteristic(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: CodeableConcept,
        exclude: boolean,
        period: Optional[Period] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param code: A code that identifies the kind of trait being asserted.
            :param exclude: If true, indicates the characteristic is one that is NOT held by members of
        the group.
            :param period: The period over which the characteristic is tested; e.g. the patient had an
        operation during the month of June.
        """
        super().__init__(
            resourceType="GroupCharacteristic",
            id_=id_,
            meta=meta,
            extension=extension,
            code=code,
            exclude=exclude,
            period=period,
        )