from __future__ import annotations
from typing import Optional, Union, List, Any, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.resource_type import ResourceType
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.backbone_elements.example_scenario_version import ExampleScenarioVersion
    from spark_auto_mapper_fhir.backbone_elements.example_scenario_contained_instance import ExampleScenarioContainedInstance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleScenarioInstance(FhirBackboneElementBase):
    """
    """
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        resourceId: string,
        resourceType: ResourceType,
        name: Optional[string] = None,
        description: Optional[markdown] = None,
        version: Optional[FhirList[ExampleScenarioVersion]] = None,
        containedInstance: Optional[FhirList[ExampleScenarioContainedInstance]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param resourceId: The id of the resource for referencing.
        :param resourceType: The type of the resource.
        :param name: A short name for the resource instance.
        :param description: Human-friendly description of the resource instance.
        :param version: A specific version of the resource.
        :param containedInstance: Resources contained in the instance (e.g. the observations contained in a
    bundle).
        """
        super().__init__(
            resourceType="ExampleScenarioInstance",
            id_=id_,
            meta=meta,
            extension=extension,
            resourceId=resourceId,
            resourceType=resourceType,
            name=name,
            description=description,
            version=version,
            containedInstance=containedInstance,
        )