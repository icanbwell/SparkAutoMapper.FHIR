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
    from spark_auto_mapper_fhir.complex_types.example_scenario_actor_type import (
        ExampleScenarioActorType,
    )
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.markdown import markdown


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleScenarioActor(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        actorId: string,
        type: ExampleScenarioActorType,
        name: Optional[string] = None,
        description: Optional[markdown] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param actorId: ID or acronym of actor.
        :param type: The type of actor - person or system.
        :param name: The name of the actor as shown in the page.
        :param description: The description of the actor.
        """
        super().__init__(
            resourceType="ExampleScenarioActor",
            id_=id_,
            meta=meta,
            extension=extension,
            actorId=actorId,
            type=type,
            name=name,
            description=description,
        )