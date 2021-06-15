from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.episodeofcare import EpisodeOfCareSchema

from spark_auto_mapper_fhir.backbone_elements.episode_of_care_status_history_backbone_element import (
    EpisodeOfCareStatusHistoryBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.account import Account
from spark_auto_mapper_fhir.resources.care_team import CareTeam
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.valuesets.diagnosis_role import DiagnosisRole
from spark_auto_mapper_fhir.valuesets.episode_of_care_status import (
    EpisodeOfCareStatusCode,
)
from spark_auto_mapper_fhir.valuesets.episode_of_care_type import EpisodeOfCareTypeCode


class EpisodeOfCare(FhirResourceBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: EpisodeOfCareStatusCode,
        statusHistory: Optional[
            FhirList[EpisodeOfCareStatusHistoryBackboneElement]
        ] = None,
        type_: Optional[FhirList[CodeableConcept[EpisodeOfCareTypeCode]]] = None,
        diagnosis: Optional[FhirList[DiagnosisRole]] = None,
        patient: Reference["Patient"],
        managingOrganization: Optional[Reference[Organization]] = None,
        period: Optional[Period] = None,
        referralRequest: Optional[FhirList[Reference[ServiceRequest]]] = None,
        careManager: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        team: Optional[FhirList[Reference[CareTeam]]] = None,
        account: Optional[FhirList[Reference[Account]]] = None,
    ) -> None:
        """
        EpisodeOfCare Resource in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/episodeofcare.html


        :param id_: id of resource
        :param identifier: Business Identifier(s) relevant for this EpisodeOfCare
        :param status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
        :param statusHistory: Past list of status codes (the current status may be included to cover the start date of the status)
        :param type_: Type/class - e.g. specialist referral, disease management
        :param diagnosis: The list of diagnosis relevant to this episode of care
        :param patient: The patient who is the focus of this episode of care
        :param managingOrganization: Organization that assumes care
        :param period: Interval during responsibility is assumed
        :param referralRequest: Originating Referral Request(s)
        :param careManager: Care manager/care coordinator for the patient
        :param team: Other practitioners facilitating this episode of care
        :param account: The set of accounts that may be used for billing for this EpisodeOfCare

        """
        super().__init__(
            resourceType="EpisodeOfCare",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            statusHistory=statusHistory,
            type_=type_,
            diagnosis=diagnosis,
            patient=patient,
            managingOrganization=managingOrganization,
            period=period,
            referralRequest=referralRequest,
            careManager=careManager,
            team=team,
            account=account,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EpisodeOfCareSchema.get_schema(include_extension=include_extension)
