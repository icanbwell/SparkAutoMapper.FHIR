from typing import Optional
from pyspark.sql.types import StructType
from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifactSchema

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUrl, FhirCanonical
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.valuesets.related_artifact_type import RelatedArtifactTypeCode


class RelatedArtifact(FhirResourceBase):
    def __init__(
        self,
        type_: RelatedArtifactTypeCode,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        label: Optional[FhirString] = None,
        display: Optional[FhirString] = None,
        citation: Optional[FhirMarkdown] = None,
        url: Optional[FhirUrl] = None,
        document: Optional[Attachment] = None,
        resource: Optional[FhirCanonical] = None
    ) -> None:
        """
        RelatedArtifact Resource in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#RelatedArtifact
        Related artifacts for a knowledge resource


        :param id_: id of resource
        :param type_: documentation | justification | citation | predecessor | successor | derived-from
                        | depends-on | composed-of
        :param label: Short label
        :param display: Brief description of the related artifact
        :param citation: Bibliographic citation for the artifact
        :param url: Where the artifact can be accessed
        :param document: What document is being referenced
        :param resource: What resource is being referenced
        """
        super().__init__(
            resourceType="RelatedArtifact",
            id_=id_,
            meta=meta,
            extension=extension,
            type_=type_,
            label=label,
            display=display,
            citation=citation,
            url=url,
            document=document,
            resource=resource
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return RelatedArtifactSchema.get_schema(
            include_extension=include_extension
        )
