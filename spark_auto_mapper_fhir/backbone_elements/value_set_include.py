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
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.backbone_elements.value_set_concept import (
        ValueSetConcept,
    )
    from spark_auto_mapper_fhir.backbone_elements.value_set_filter import ValueSetFilter
    from spark_auto_mapper_fhir.complex_types.canonical import canonical


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetInclude(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        system: Optional[uri] = None,
        version: Optional[string] = None,
        concept: Optional[FhirList[ValueSetConcept]] = None,
        filter: Optional[FhirList[ValueSetFilter]] = None,
        valueSet: Optional[FhirList[canonical]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param system: An absolute URI which is the code system from which the selected codes come
        from.
            :param version: The version of the code system that the codes are selected from, or the
        special version '*' for all versions.
            :param concept: Specifies a concept to be included or excluded.
            :param filter: Select concepts by specify a matching criterion based on the properties
        (including relationships) defined by the system, or on filters defined by the
        system. If multiple filters are specified, they SHALL all be true.
            :param valueSet: Selects the concepts found in this value set (based on its value set
        definition). This is an absolute URI that is a reference to ValueSet.url.  If
        multiple value sets are specified this includes the union of the contents of
        all of the referenced value sets.
        """
        super().__init__(
            resourceType="ValueSetInclude",
            id_=id_,
            meta=meta,
            extension=extension,
            system=system,
            version=version,
            concept=concept,
            filter=filter,
            valueSet=valueSet,
        )