from __future__ import annotations
from typing import Optional, Union, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.encounter import EncounterSchema

from spark_auto_mapper_fhir.backbone_elements.encounter_class_history_backbone_element import (
    EncounterClassHistoryBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.encounter_hospitalization_backbone_element import (
    EncounterHospitalizationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.encounter_location_backbone_element import (
    EncounterLocationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.encounter_participant_backbone_element import (
    EncounterParticipantBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.encounter_status_history_backbone_element import (
    EncounterStatusHistoryBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.encounter_diagnosis_backbone_element import (
    EncounterDiagnosisBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.duration import Duration
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.resources.episode_of_care import (
    EpisodeOfCare,
)  # To be added after EOC is merged
from spark_auto_mapper_fhir.resources.account import Account
from spark_auto_mapper_fhir.resources.appointment import Appointment

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.immunization_recommendation import (
    ImmunizationRecommendation,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.valuesets.encounter_class_code import EncounterClassCode
from spark_auto_mapper_fhir.valuesets.encounter_reason import EncounterReasonCode
from spark_auto_mapper_fhir.valuesets.encounter_service_type import (
    EncounterServiceTypeCode,
)
from spark_auto_mapper_fhir.valuesets.encounter_status import EncounterStatusCode
from spark_auto_mapper_fhir.valuesets.encounter_type_code import EncounterTypeCode
from spark_auto_mapper_fhir.valuesets.v3_act_priority import V3ActPriorityCode


class Encounter(FhirResourceBase):
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: EncounterStatusCode,
        statusHistory: Optional[FhirList[EncounterStatusHistoryBackboneElement]] = None,
        class_: EncounterClassCode,
        classHistory: Optional[FhirList[EncounterClassHistoryBackboneElement]] = None,
        type_: Optional[FhirList[CodeableConcept[EncounterTypeCode]]] = None,
        serviceType: Optional[CodeableConcept[EncounterServiceTypeCode]] = None,
        priority: Optional[CodeableConcept[V3ActPriorityCode]] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        episodeOfCare: Optional[FhirList[Reference[EpisodeOfCare]]] = None,
        basedOn: Optional[FhirList[Reference[ServiceRequest]]] = None,
        participant: Optional[FhirList[EncounterParticipantBackboneElement]] = None,
        appointment: Optional[FhirList[Reference[Appointment]]] = None,
        period: Optional[Period] = None,
        length: Optional[Duration] = None,
        reasonCode: Optional[FhirList[CodeableConcept[EncounterReasonCode]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Procedure, Observation, ImmunizationRecommendation]
                ]
            ]
        ] = None,
        diagnosis: Optional[FhirList[EncounterDiagnosisBackboneElement]] = None,
        account: Optional[FhirList[Reference[Account]]] = None,
        hospitalization: Optional[EncounterHospitalizationBackboneElement] = None,
        location: Optional[FhirList[EncounterLocationBackboneElement]] = None,
        serviceProvider: Optional[Reference[Organization]] = None,
        partOf: Optional[Reference[Encounter]] = None,
    ) -> None:
        """
        Encounter Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Encounter


        :param id_: id of resource
        :param identifier: External Ids for this condition
        :param status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +
        :param statusHistory: List of past encounter classes
        :param class_: Classification of patient encounter
        :param classHistory: List of past encounter classes
        :param type_: Specific type of encounter
        :param serviceType: Specific type of service
        :param priority: Indicates the urgency of the encounter
        :param subject: The patient or group present at the encounter
        :param episodeOfCare: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
        :param basedOn: The ServiceRequest that initiated this encounter
        :param participant: List of participants involved in the encounter
        :param appointment: The appointment that scheduled this encounter
        :param period: The start and end time of the encounter
        :param length: Quantity of time the encounter lasted (less time absent)
        :param reasonCode: Coded reason the encounter takes place
        :param reasonReference: Reason the encounter takes place (reference)
        :param diagnosis: The list of diagnosis relevant to this encounter
        :param account: The set of accounts that may be used for billing for this Encounter
        :param hospitalization: Details about the admission to a healthcare service
        :param location: List of locations where the patient has been
        :param serviceProvider: The organization (facility) responsible for this encounter
        :param partOf: Another Encounter this encounter is part of

        """
        super().__init__(
            resourceType="Encounter",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            statusHistory=statusHistory,
            class_=class_,
            classHistory=classHistory,
            type_=type_,
            serviceType=serviceType,
            priority=priority,
            subject=subject,
            episodeOfCare=episodeOfCare,
            basedOn=basedOn,
            participant=participant,
            appointment=appointment,
            period=period,
            length=length,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            diagnosis=diagnosis,
            account=account,
            hospitalization=hospitalization,
            location=location,
            serviceProvider=serviceProvider,
            partOf=partOf,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EncounterSchema.get_schema(include_extension=include_extension)
