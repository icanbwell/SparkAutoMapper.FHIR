from typing import Optional, Union, Any

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.appointment import AppointmentSchema
from spark_fhir_schemas.r4.resources.location import LocationSchema

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.backbone_elements.hours_of_operation_backbone_element import (
    HoursOfOperationBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.participant_backbone_element import ParticipantBackboneElement
from spark_auto_mapper_fhir.backbone_elements.position_backbone_element import (
    PositionBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt
from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.immunization_recommendation import ImmunizationRecommendation
from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.resources.slot import Slot
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.appointment_cancellation_reason import AppointmentCancellationReasonCode
from spark_auto_mapper_fhir.valuesets.appointment_status import AppointmentStatusCode
from spark_auto_mapper_fhir.valuesets.encounter_reason import EncounterReasonCode
from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode
from spark_auto_mapper_fhir.valuesets.service_category import ServiceCategoryCode
from spark_auto_mapper_fhir.valuesets.service_type import ServiceTypeCode
from spark_auto_mapper_fhir.valuesets.v2_appointment_reason import V2AppointmentReasonCode


class Appointment(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: [AppointmentStatusCode],
        cancelationReason: Optional[AppointmentCancellationReasonCode] = None,
        serviceCategory: Optional[FhirList[CodeableConcept[ServiceCategoryCode]]] = None,
        serviceType: Optional[FhirList[CodeableConcept[ServiceTypeCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]] = None,
        appointmentType: Optional[CodeableConcept[V2AppointmentReasonCode]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[EncounterReasonCode]]] = None,
        reasonReference: Optional[FhirList[Reference[Union[Condition, Procedure, Observation, ImmunizationRecommendation]]]] = None,
        priority: Optional[FhirUnsignedInt] = None,
        description: Optional[FhirString] = None,
        supportingInformation: Optional[FhirList[Reference[Any]]] = None,
        start: Optional[FhirInstant] = None,
        end: Optional[FhirInstant] = None,
        minutesDuration: Optional[FhirPositiveInt] = None,
        slot: Optional[FhirList[Reference[Slot]]] = None,
        created: Optional[FhirDateTime] = None,
        comment: Optional[FhirString] = None,
        patientInstruction: Optional[FhirString] = None,
        basedOn: Optional[FhirList[Reference[ServiceRequest]]] = None,
        participant: [FhirList[ParticipantBackboneElement]],
        requestedPeriod: Optional[FhirList[Period]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Appointment Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Appointment



        :param id_: id of resource
        :param identifier:
        :param status:
        :param endpoint: Technical endpoints providing access to services operated for the location
        """
        super().__init__(
            resourceType="Appointment",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            cancelationReason=cancelationReason,
            serviceCategory=serviceCategory,
            serviceType=serviceType,
            specialty=specialty,
            appointmentType=appointmentType,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            priority=priority,
            description=description,
            supportingInformation=supportingInformation,
            start=start,
            end=end,
            minutesDuration=minutesDuration,
            slot=slot,
            created=created,
            comment=comment,
            patientInstruction=patientInstruction,
            basedOn=basedOn,
            participant=participant,
            requestedPeriod=requestedPeriod,
            endpoint=endpoint,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AppointmentSchema.get_schema(include_extension=include_extension)
