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
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.string import string


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleScenarioContainedInstance(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        resourceId: string,
        versionId: Optional[string] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param resourceId: Each resource contained in the instance.
        :param versionId: A specific version of a resource contained in the instance.
        """
        super().__init__(
            resourceType="ExampleScenarioContainedInstance",
            id_=id_,
            meta=meta,
            extension=extension,
            resourceId=resourceId,
            versionId=versionId,
        )