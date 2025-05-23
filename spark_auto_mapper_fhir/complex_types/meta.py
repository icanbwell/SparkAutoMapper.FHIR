from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_fhir_schemas.r4.complex_types.meta import MetaSchema


if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # versionId (id)
    # lastUpdated (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # source (uri)
    # profile (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # security (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for security
    from spark_auto_mapper_fhir.value_sets.all_security_labels import (
        AllSecurityLabelsCode,
    )

    # End Import for CodeableConcept for security
    # tag (Coding)
    # Import for CodeableConcept for tag
    from spark_auto_mapper_fhir.value_sets.common_tags import CommonTagsCode

    # End Import for CodeableConcept for tag


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Meta(FhirComplexTypeBase):
    """
    Meta
    fhir-base.xsd
        The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[NestedExtensionItem]] = None,
        versionId: Optional[FhirId] = None,
        lastUpdated: Optional[FhirInstant] = None,
        source: Optional[FhirUri] = None,
        profile: Optional[FhirList[FhirCanonical]] = None,
        security: Optional[FhirList[Coding[AllSecurityLabelsCode]]] = None,
        tag: Optional[FhirList[Coding[CommonTagsCode]]] = None,
    ) -> None:
        """
            The metadata about a resource. This is content in the resource that is
        maintained by the infrastructure. Changes to the content might not always be
        associated with version changes to the resource.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param versionId: The version specific identifier, as it appears in the version portion of the
        URL. This value changes when the resource is created, updated, or deleted.
            :param lastUpdated: When the resource last changed - e.g. when the version changed.
            :param source: A uri that identifies the source system of the resource. This provides a
        minimal amount of [[[Provenance]]] information that can be used to track or
        differentiate the source of information in the resource. The source may
        identify another FHIR server, document, message, database, etc.
            :param profile: A list of profiles (references to [[[StructureDefinition]]] resources) that
        this resource claims to conform to. The URL is a reference to
        [[[StructureDefinition.url]]].
            :param security: Security labels applied to this resource. These tags connect specific
        resources to the overall security policy and infrastructure.
            :param tag: Tags applied to this resource. Tags are intended to be used to identify and
        relate resources to process and workflow, and applications are not required to
        consider the tags when interpreting the meaning of a resource.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            versionId=versionId,
            lastUpdated=lastUpdated,
            source=source,
            profile=profile,
            security=security,
            tag=tag,
        )
        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return MetaSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
