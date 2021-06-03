from typing import Optional, Union

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item_backbone_element import (
        QuestionnaireResponseItemBackboneElement,
    )
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class QuestionnaireResponseItemAnswerBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        value: Optional[
            Union[
                FhirBoolean,
                FhirDecimal,
                FhirInteger,
                FhirDate,
                FhirDateTime,
                FhirString,
                FhirUri,
                FhirReference,
            ]
        ] = None,
        item: Optional[FhirList["QuestionnaireResponseItemBackboneElement"]] = None,
    ) -> None:
        """
        QuestionnaireResponseItemAnswerBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR properties not just the ones you need
        https://www.hl7.org/fhir/questionnaireresponse-definitions.html#QuestionnaireResponse.item.answer

        :param value: Single-valued answer to the question
        :param item: Nested groups and questions
        """
        super().__init__(id_=id_, extension=extension, value=value, item=item)
