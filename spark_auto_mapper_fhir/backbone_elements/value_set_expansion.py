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
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.date_time import dateTime
    from spark_auto_mapper_fhir.complex_types.integer import integer
    from spark_auto_mapper_fhir.complex_types.integer import integer
    from spark_auto_mapper_fhir.backbone_elements.value_set_parameter import (
        ValueSetParameter,
    )
    from spark_auto_mapper_fhir.backbone_elements.value_set_contains import (
        ValueSetContains,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetExpansion(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[uri] = None,
        timestamp: dateTime,
        total: Optional[integer] = None,
        offset: Optional[integer] = None,
        parameter: Optional[FhirList[ValueSetParameter]] = None,
        contains: Optional[FhirList[ValueSetContains]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: An identifier that uniquely identifies this expansion of the valueset, based
        on a unique combination of the provided parameters, the system default
        parameters, and the underlying system code system versions etc. Systems may
        re-use the same identifier as long as those factors remain the same, and the
        expansion is the same, but are not required to do so. This is a business
        identifier.
            :param timestamp: The time at which the expansion was produced by the expanding system.
            :param total: The total number of concepts in the expansion. If the number of concept nodes
        in this resource is less than the stated number, then the server can return
        more using the offset parameter.
            :param offset: If paging is being used, the offset at which this resource starts.  I.e. this
        resource is a partial view into the expansion. If paging is not being used,
        this element SHALL NOT be present.
            :param parameter: A parameter that controlled the expansion process. These parameters may be
        used by users of expanded value sets to check whether the expansion is
        suitable for a particular purpose, or to pick the correct expansion.
            :param contains: The codes that are contained in the value set expansion.
        """
        super().__init__(
            resourceType="ValueSetExpansion",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            timestamp=timestamp,
            total=total,
            offset=offset,
            parameter=parameter,
            contains=contains,
        )