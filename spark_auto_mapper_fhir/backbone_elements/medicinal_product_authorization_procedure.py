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
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_authorization_procedure import (
        MedicinalProductAuthorizationProcedure,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductAuthorizationProcedure(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        type: CodeableConcept,
        application: Optional[FhirList[MedicinalProductAuthorizationProcedure]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param identifier: Identifier for this procedure.
        :param type: Type of procedure.
        :param application: Applcations submitted to obtain a marketing authorization.
        """
        super().__init__(
            resourceType="MedicinalProductAuthorizationProcedure",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            type=type,
            application=application,
        )