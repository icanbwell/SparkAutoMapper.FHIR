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
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.id import id
    from spark_auto_mapper_fhir.complex_types.string import string


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImplementationGuideDependsOn(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        uri: canonical,
        packageId: Optional[id] = None,
        version: Optional[string] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param uri: A canonical reference to the Implementation guide for the dependency.
            :param packageId: The NPM package name for the Implementation Guide that this IG depends on.
            :param version: The version of the IG that is depended on, when the correct version is
        required to understand the IG correctly.
        """
        super().__init__(
            resourceType="ImplementationGuideDependsOn",
            id_=id_,
            meta=meta,
            extension=extension,
            uri=uri,
            packageId=packageId,
            version=version,
        )