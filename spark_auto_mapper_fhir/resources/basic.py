from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.basic import BasicSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.complex_types.basic_resource_type import (
        BasicResourceType,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.date import FhirDate
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for author
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Basic(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        code: CodeableConcept[BasicResourceType],
        subject: Optional[Reference[Union[Resource]]] = None,
        created: Optional[FhirDate] = None,
        author: Optional[
            Reference[
                Union[
                    Practitioner, PractitionerRole, Patient, RelatedPerson, Organization
                ]
            ]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Identifier assigned to the resource for business purposes, outside the context
        of FHIR.
            :param code: Identifies the 'type' of resource - equivalent to the resource name for other
        resources.
            :param subject: Identifies the patient, practitioner, device or any other resource that is the
        "focus" of this resource.
            :param created: Identifies when the resource was first created.
            :param author: Indicates who was responsible for creating the resource instance.
        """
        super().__init__(
            resourceType="Basic",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            code=code,
            subject=subject,
            created=created,
            author=author,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return BasicSchema.get_schema(include_extension=include_extension)