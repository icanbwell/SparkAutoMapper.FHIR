from typing import Optional, Union, Any

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.appointment import AppointmentSchema

from spark_auto_mapper_fhir.backbone_elements.appointment_participant_backbone_element import (
    AppointmentParticipantBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt
from spark_auto_mapper_fhir.resources.condition import Condition
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.immunization_recommendation import (
    ImmunizationRecommendation,
)
from spark_auto_mapper_fhir.resources.observation import Observation
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.resources.slot import Slot
from spark_auto_mapper_fhir.valuesets.appointment_cancellation_reason import (
    AppointmentCancellationReasonCode,
)
from spark_auto_mapper_fhir.valuesets.appointment_status import AppointmentStatusCode
from spark_auto_mapper_fhir.valuesets.encounter_reason import EncounterReasonCode
from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode
from spark_auto_mapper_fhir.valuesets.service_category import ServiceCategoryCode
from spark_auto_mapper_fhir.valuesets.service_type import ServiceTypeCode
from spark_auto_mapper_fhir.valuesets.v2_appointment_reason import (
    V2AppointmentReasonCode,
)


class Appointment(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: AppointmentStatusCode,
        cancelationReason: Optional[AppointmentCancellationReasonCode] = None,
        serviceCategory: Optional[
            FhirList[CodeableConcept[ServiceCategoryCode]]
        ] = None,
        serviceType: Optional[FhirList[CodeableConcept[ServiceTypeCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]] = None,
        appointmentType: Optional[CodeableConcept[V2AppointmentReasonCode]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[EncounterReasonCode]]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Procedure, Observation, ImmunizationRecommendation]
                ]
            ]
        ] = None,
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
        participant: FhirList[AppointmentParticipantBackboneElement],
        requestedPeriod: Optional[FhirList[Period]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Appointment Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Appointment
        A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s)


        :param id_: id of resource
        :param identifier: External Ids for this item
        :param status: proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
        :param cancelationReason: The coded reason for the appointment being cancelled
        :param serviceCategory: A broad categorization of the service that is to be performed during this appointment
        :param serviceType: The specific service that is to be performed during this appointment
        :param specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
        :param appointmentType: The style of appointment or patient that has been booked in the slot (not service type)
        :param reasonCode: Coded reason this appointment is scheduled
        :param reasonReference: Reason the appointment is to take place (resource)
        :param priority: Used to make informed decisions if needing to re-prioritize
        :param description: Shown on a subject line in a meeting request, or appointment list
        :param supportingInformation: Additional information to support the appointment
        :param start: When appointment is to take place
        :param end: When appointment is to conclude
        :param minutesDuration: Can be less than start/end (e.g. estimate)
        :param slot: The slots that this appointment is filling
        :param created: The date that this appointment was initially created
        :param comment: Additional comments
        :param patientInstruction: Detailed information and instructions for the patient
        :param basedOn: The service request this appointment is allocated to assess
        :param participant: Participants involved in appointment
            + Rule: Either the type or actor on the participant SHALL be specified
        :param requestedPeriod: Potential date/time interval(s) requested to allocate the appointment within

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
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AppointmentSchema.get_schema(include_extension=include_extension)
