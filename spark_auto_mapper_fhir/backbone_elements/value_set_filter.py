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
    from spark_auto_mapper_fhir.complex_types.filter_operator import FilterOperator
    from spark_auto_mapper_fhir.complex_types.string import string


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetFilter(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        property: code,
        op: FilterOperator,
        value: string,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param property: A code that identifies a property or a filter defined in the code system.
            :param op: The kind of operation to perform as a part of the filter criteria.
            :param value: The match value may be either a code defined by the system, or a string value,
        which is a regex match on the literal string of the property value  (if the
        filter represents a property defined in CodeSystem) or of the system filter
        value (if the filter represents a filter defined in CodeSystem) when the
        operation is 'regex', or one of the values (true and false), when the
        operation is 'exists'.
        """
        super().__init__(
            resourceType="ValueSetFilter",
            id_=id_,
            meta=meta,
            extension=extension,
            property=property,
            op=op,
            value=value,
        )