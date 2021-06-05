from typing import Optional, Union

from pyspark.sql.types import StructType, DataType

from spark_auto_mapper_fhir.backbone_elements.group_member_backbone_element import (
    GroupMemberBackboneElement,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.resources.group import GroupSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.valuesets.group_type import GroupTypeCode

from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A


class Group(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        type_: Optional[GroupTypeCode] = None,
        name: Optional[FhirString] = None,
        member: Optional[FhirList[GroupMemberBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        Group Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Group


        :param id_: id of resource
        """
        super().__init__(
            resourceType="Group",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            type_=type_,
            name=name,
            member=member,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return GroupSchema.get_schema(include_extension=include_extension)

    id_: FhirId = FhirId(A.column("id_"))
    identifier = A.column("identifier")
    name = A.column("name")
    type_ = A.column("type_")
    member = A.column("member")
