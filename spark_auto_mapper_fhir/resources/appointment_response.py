from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.appointmentresponse import (
    AppointmentResponseSchema,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for appointment
    from spark_auto_mapper_fhir.resources.appointment import Appointment
    from spark_auto_mapper_fhir.complex_types.instant import instant
    from spark_auto_mapper_fhir.complex_types.instant import instant
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for participantType
    from spark_auto_mapper_fhir.complex_types.participant_type import ParticipantType
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for actor
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.participation_status import (
        ParticipationStatus,
    )
    from spark_auto_mapper_fhir.complex_types.string import FhirString


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AppointmentResponse(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        appointment: Reference[Union[Appointment]],
        start: Optional[instant] = None,
        end: Optional[instant] = None,
        participantType: Optional[FhirList[CodeableConcept[ParticipantType]]] = None,
        actor: Optional[
            Reference[
                Union[
                    Patient,
                    Practitioner,
                    PractitionerRole,
                    RelatedPerson,
                    Device,
                    HealthcareService,
                    Location,
                ]
            ]
        ] = None,
        participantStatus: ParticipationStatus,
        comment: Optional[FhirString] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: This records identifiers associated with this appointment response concern
        that are defined by business processes and/ or used to refer to it when a
        direct URL reference to the resource itself is not appropriate.
            :param appointment: Appointment that this response is replying to.
            :param start: Date/Time that the appointment is to take place, or requested new start time.
            :param end: This may be either the same as the appointment request to confirm the details
        of the appointment, or alternately a new time to request a re-negotiation of
        the end time.
            :param participantType: Role of participant in the appointment.
            :param actor: A Person, Location, HealthcareService, or Device that is participating in the
        appointment.
            :param participantStatus: Participation status of the participant. When the status is declined or
        tentative if the start/end times are different to the appointment, then these
        times should be interpreted as a requested time change. When the status is
        accepted, the times can either be the time of the appointment (as a
        confirmation of the time) or can be empty.
            :param comment: Additional comments about the appointment.
        """
        super().__init__(
            resourceType="AppointmentResponse",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            appointment=appointment,
            start=start,
            end=end,
            participantType=participantType,
            actor=actor,
            participantStatus=participantStatus,
            comment=comment,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AppointmentResponseSchema.get_schema(include_extension=include_extension)