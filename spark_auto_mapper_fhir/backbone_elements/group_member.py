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
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for entity
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.complex_types.boolean import boolean


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GroupMember(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        entity: Reference[
            Union[
                Patient,
                Practitioner,
                PractitionerRole,
                Device,
                Medication,
                Substance,
                Group,
            ]
        ],
        period: Optional[Period] = None,
        inactive: Optional[boolean] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param entity: A reference to the entity that is a member of the group. Must be consistent
        with Group.type. If the entity is another group, then the type must be the
        same.
            :param period: The period that the member was in the group, if known.
            :param inactive: A flag to indicate that the member is no longer in the group, but previously
        may have been a member.
        """
        super().__init__(
            resourceType="GroupMember",
            id_=id_,
            meta=meta,
            extension=extension,
            entity=entity,
            period=period,
            inactive=inactive,
        )