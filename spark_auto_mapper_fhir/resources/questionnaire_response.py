from typing import Optional, Any, Union
from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.questionnaireresponse import QuestionnaireResponseSchema

from spark_auto_mapper_fhir.backbone_elements.questionnaire_response_item_backbone_element import \
    QuestionnaireResponseItemBackboneElement
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.care_plan import CarePlan
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.resources.questionnaire import Questionnaire
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.valuesets.questionnaire_answers_status import QuestionnaireAnswersStatusCode


class QuestionnaireResponse(FhirResourceBase):
    def __init__(
        self,
        status: QuestionnaireAnswersStatusCode,
        identifier: Optional[Identifier] = None,
        based_on: Optional[FhirList[Reference[Union[CarePlan,
                                                    ServiceRequest]]]] = None,
        part_of: Optional[FhirList[Reference[Union['Observation',
                                                   Procedure]]]] = None,
        questionnaire: Optional[Reference[Questionnaire]] = None,
        subject: Optional[Reference[Any]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        authored: Optional[FhirDate] = None,
        author: Optional[Reference[Union[Device, Practitioner,
                                         PractitionerRole, Patient,
                                         RelatedPerson, Organization]]] = None,
        source: Optional[Reference[Union[Patient, Practitioner,
                                         PractitionerRole,
                                         RelatedPerson]]] = None,
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
        :param based_on: The order, proposal or plan that is fulfilled in whole or in part by this QuestionnaireResponse. For example, a ServiceRequest seeking an intake assessment or a decision support recommendation to assess for post-partum depression.
        :param part_of: A procedure or observation that this questionnaire was performed as part of the execution of. For example, the surgery a checklist was executed as part of.
        :param questionnaire: The Questionnaire that defines and organizes the questions for which answers are being provided.
        :param subject: The subject of the questionnaire response. This could be a patient, organization, practitioner, device, etc. This is who/what the answers apply to, but is not necessarily the source of information.
        :param encounter: The Encounter during which this questionnaire response was created or to which the creation of this record is tightly associated.
        :param authored: The date and/or time that this set of answers were last changed.,
        :param author: Person who received the answers to the questions in the QuestionnaireResponse and recorded them in the system.
        :param source: The person who answered the questions about the subject.
        :param item: A group or question item from the original questionnaire for which answers are provided.

        """
        super().__init__(
            resourceType="QuestionnaireResponse",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            based_on=based_on,
            part_of=part_of,
            questionnaire=questionnaire,
            status=status,
            subject=subject,
            encounter=encounter,
            authored=authored,
            author=author,
            source=source,
            item=item
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return QuestionnaireResponseSchema.get_schema(
            include_extension=include_extension
        )
