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
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for detail
    from spark_auto_mapper_fhir.resources.resource import Resource


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CompositionEvent(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[FhirList[CodeableConcept]] = None,
        period: Optional[Period] = None,
        detail: Optional[FhirList[Reference[Union[Resource]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param code: This list of codes represents the main clinical acts, such as a colonoscopy or
        an appendectomy, being documented. In some cases, the event is inherent in the
        typeCode, such as a "History and Physical Report" in which the procedure being
        documented is necessarily a "History and Physical" act.
            :param period: The period of time covered by the documentation. There is no assertion that
        the documentation is a complete representation for this period, only that it
        documents events during this time.
            :param detail: The description and/or reference of the event(s) being documented. For
        example, this could be used to document such a colonoscopy or an appendectomy.
        """
        super().__init__(
            resourceType="CompositionEvent",
            id_=id_,
            meta=meta,
            extension=extension,
            code=code,
            period=period,
            detail=detail,
        )