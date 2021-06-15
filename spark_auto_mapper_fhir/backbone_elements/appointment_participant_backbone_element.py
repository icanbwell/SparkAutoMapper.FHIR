from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.encounter_participant_type import (
    EncounterParticipantTypeCode,
)
from spark_auto_mapper_fhir.valuesets.participant_required import (
    ParticipantRequiredCode,
)
from spark_auto_mapper_fhir.valuesets.participation_status import (
    ParticipationStatusCode,
)


class AppointmentParticipantBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        type_: Optional[FhirList[CodeableConcept[EncounterParticipantTypeCode]]] = None,
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
        required: Optional[ParticipantRequiredCode] = None,
        status: ParticipationStatusCode,
        period: Optional[Period] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        AppointmentParticipant Backbone Element in FHIR
        https://www.hl7.org/fhir/appointment.html#Appointment.participant
        Participants involved in appointment


        :param type_: Role of participant in the appointment
        :param actor: Person, Location/HealthcareService or Device
        :param required: required | optional | information-only
        :param status: accepted | declined | tentative | needs-action
        :param period: Participation period of the actor
        """
        super().__init__(
            id_=id_,
            type_=type_,
            actor=actor,
            required=required,
            status=status,
            period=period,
            extension=extension,
        )
