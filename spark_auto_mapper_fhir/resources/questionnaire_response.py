from typing import Optional, Any
from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.questionnaireresponse import QuestionnaireResponseSchema

from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item_backbone_element import \
    QuestionnaireResponseItemBackboneElement
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.valuesets.questionnaire_answers_status import QuestionnaireAnswersStatusCode


class QuestionnaireResponse(FhirResourceBase):
    def __init__(
        self,
        status: QuestionnaireAnswersStatusCode,
        identifier: Optional[Identifier] = None,
        subject: Optional[Reference[Any]] = None,
        authored: Optional[FhirDate] = None,
        item: Optional[FhirList[QuestionnaireResponseItemBackboneElement]
                       ] = None,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
    ) -> None:
        """
        QuestionnaireResponse Resource in FHIR
        https://www.hl7.org/fhir/questionnaireresponse.html


        :param id_: id of resource
        :param status: The position of the questionnaire response within its overall lifecycle.
        :param identifier: A business identifier assigned to a particular completed (or partially completed) questionnaire.
        :param subject: The subject of the questionnaire response. This could be a patient, organization, practitioner, device, etc. This is who/what the answers apply to, but is not necessarily the source of information.
        :param authored: The date and/or time that this set of answers were last changed.,
        :param item: A group or question item from the original questionnaire for which answers are provided.

        """
        super().__init__(
            resourceType="QuestionnaireResponse",
            id_=id_,
            meta=meta,
            extension=extension,
            status=status,
            identifier=identifier,
            subject=subject,
            authored=authored,
            item=item
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return QuestionnaireResponseSchema.get_schema(
            include_extension=include_extension
        )
