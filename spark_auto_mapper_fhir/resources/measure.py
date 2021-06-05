from typing import Optional, Union
from pyspark.sql.types import StructType, DataType

from spark_auto_mapper_fhir.valuesets.measure_improvement_notation import (
    MeasureImprovementNotationCode,
)
from spark_auto_mapper_fhir.valuesets.subject_type import SubjectTypeCode

from spark_auto_mapper_fhir.resources.related_artifact import RelatedArtifact

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.date import FhirDate

from spark_auto_mapper_fhir.valuesets.jurisdiction import JurisdictionCode

from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean

from spark_auto_mapper_fhir.valuesets.definition_topic import DefinitionTopicCode

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.complex_types.identifier import Identifier

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri, FhirCanonical

from spark_auto_mapper_fhir.valuesets.publication_status import PublicationStatusCode
from spark_fhir_schemas.r4.resources.measure import MeasureSchema

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta


class Measure(FhirResourceBase):
    def __init__(
        self,
        status: PublicationStatusCode,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        url: Optional[FhirUri] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        version: Optional[FhirString] = None,
        name: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        subtitle: Optional[FhirString] = None,
        experimental: Optional[FhirBoolean] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
        date: Optional[FhirDateTime] = None,
        publisher: Optional[FhirString] = None,
        contact: Optional[FhirList[ContactDetail]] = None,
        description: Optional[FhirMarkdown] = None,
        useContext: Optional[FhirList[UsageContext]] = None,
        jurisdiction: Optional[FhirList[CodeableConcept[JurisdictionCode]]] = None,
        purpose: Optional[FhirMarkdown] = None,
        usage: Optional[FhirString] = None,
        copyright_: Optional[FhirMarkdown] = None,
        approvalDate: Optional[FhirDate] = None,
        lastReviewDate: Optional[FhirDate] = None,
        effectivePeriod: Optional[Period] = None,
        topic: Optional[FhirList[CodeableConcept[DefinitionTopicCode]]] = None,
        author: Optional[FhirList[ContactDetail]] = None,
        editor: Optional[FhirList[ContactDetail]] = None,
        reviewer: Optional[FhirList[ContactDetail]] = None,
        endorser: Optional[FhirList[ContactDetail]] = None,
        relatedArtifact: Optional[FhirList[RelatedArtifact]] = None,
        library: Optional[FhirList[FhirCanonical]] = None,
        disclaimer: Optional[FhirMarkdown] = None,
        # scoring: Optional[CodeableConcept[MeasureScoringCode]] = None,
        # compositeScoring: Optional[CodeableConcept[CompositeMeasureScoringCode]] = None,
        type_: Optional[FhirList[CodeableConcept[DefinitionTopicCode]]] = None,
        riskAdjustment: Optional[FhirString] = None,
        rateAggregation: Optional[FhirString] = None,
        rationale: Optional[FhirMarkdown] = None,
        clinicalRecommendationStatement: Optional[FhirMarkdown] = None,
        improvementNotation: Optional[
            CodeableConcept[MeasureImprovementNotationCode]
        ] = None,
        definition: Optional[FhirList[FhirMarkdown]] = None,
        guidance: Optional[FhirMarkdown] = None,
        # group: Optional[GroupBackboneElement] = None,
        # supplementalData Optional[SupplementalDataBackboneElement] = None,
        extension: Optional[FhirList[Extension]] = None,
    ) -> None:
        """
        Measure Resource in FHIR
        https://www.hl7.org/fhir/measure.html

        :param id_: id of resource
        """
        super().__init__(
            resourceType="Measure",
            id_=id_,
            meta=meta,
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            subtitle=subtitle,
            status=status,
            experimental=experimental,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            usage=usage,
            copyright_=copyright_,
            approvalDate=approvalDate,
            lastReviewDate=lastReviewDate,
            effectivePeriod=effectivePeriod,
            topic=topic,
            author=author,
            editor=editor,
            reviewer=reviewer,
            endorser=endorser,
            relatedArtifact=relatedArtifact,
            library=library,
            disclaimer=disclaimer,
            # scoring=scoring,
            # compositeScoring=compositeScoring,
            type_=type_,
            riskAdjustment=riskAdjustment,
            rateAggregation=rateAggregation,
            rationale=rationale,
            clinicalRecommendationStatement=clinicalRecommendationStatement,
            improvementNotation=improvementNotation,
            definition=definition,
            guidance=guidance,
            # group=group,
            # supplementalData=supplementalData,
            extension=extension,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MeasureSchema.get_schema(include_extension=include_extension)
