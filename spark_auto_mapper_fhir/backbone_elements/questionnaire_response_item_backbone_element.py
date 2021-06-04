from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item_answer_backbone_element import (
    QuestionnaireResponseItemAnswerBackboneElement,
)
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class QuestionnaireResponseItemBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        link_id: Optional[FhirString] = None,
        definition: Optional[FhirUri] = None,
        text: Optional[FhirString] = None,
        answer: Optional[
            FhirList["QuestionnaireResponseItemAnswerBackboneElement"]
        ] = None,
        item: Optional[FhirList["QuestionnaireResponseItemBackboneElement"]] = None,
    ) -> None:
        """
        QuestionnaireResponseItemBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR properties not just the ones you need
        https://www.hl7.org/fhir/questionnaireresponse-definitions.html#QuestionnaireResponse.item

        :param link_id: The item from the Questionnaire that corresponds to this item in the QuestionnaireResponse resource.
        :param definition: 	A reference to an ElementDefinition that provides the details for the item.
        :param text: Text that is displayed above the contents of the group or as the text of the question being answered.
        :param answer: The response(s) to the question
        :param item: Nested questionnaire response items
        """
        super().__init__(
            id_=id_,
            extension=extension,
            link_id=link_id,
            definition=definition,
            text=text,
            answer=answer,
            item=item,
        )
