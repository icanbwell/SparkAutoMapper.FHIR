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
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.markdown import markdown


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatementSecurity(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        cors: Optional[boolean] = None,
        service: Optional[FhirList[CodeableConcept]] = None,
        description: Optional[markdown] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param cors: Server adds CORS headers when responding to requests - this enables Javascript
        applications to use the server.
            :param service: Types of security services that are supported/required by the system.
            :param description: General description of how security works.
        """
        super().__init__(
            resourceType="CapabilityStatementSecurity",
            id_=id_,
            meta=meta,
            extension=extension,
            cors=cors,
            service=service,
            description=description,
        )