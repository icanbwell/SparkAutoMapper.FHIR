from typing import Optional, Union, TYPE_CHECKING

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.participant_role import ParticipantRoleCode


class CareTeamParticipantBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        role: Optional[FhirList[CodeableConcept[ParticipantRoleCode]]] = None,
        member: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    RelatedPerson,
                    Patient,
                    Organization,
                    "CareTeam",
                ]
            ]
        ] = None,
        onBehalfOf: Optional[Reference[Organization]] = None,
        period: Optional[Period] = None,
    ) -> None:
        """
        CareTeamParticipantBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://www.hl7.org/fhir/careteam-definitions.html#CareTeam.participant

        :param role: Type of involvement
        :param member: Who is involved
        :param onBehalfOf: Organization of the practitioner
        :param period: Time period of participant
        """
        super().__init__(
            id_=id_,
            extension=extension,
            role=role,
            member=member,
            onBehalfOf=onBehalfOf,
            period=period,
        )
