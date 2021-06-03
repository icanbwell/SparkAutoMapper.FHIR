from typing import Optional, Union, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.careteam import CareTeamSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.backbone_elements.care_team_participant_backbone_element import (
        CareTeamParticipantBackboneElement,
    )
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.encounter import Encounter

from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.valuesets.care_team_category import CareTeamCategoryCode
from spark_auto_mapper_fhir.valuesets.care_team_status import CareTeamStatusCode
from spark_auto_mapper_fhir.valuesets.snomed_clinical_finding import (
    SNOMEDCTClinicalFindingsCode,
)


class CareTeam(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: Optional[CareTeamStatusCode] = None,
        category: Optional[FhirList[CodeableConcept[CareTeamCategoryCode]]] = None,
        name: Optional[FhirString] = None,
        subject: Optional[Reference[Union[Patient, Group]]] = None,
        encounter: Optional[Reference["Encounter"]] = None,
        period: Optional[Period] = None,
        participant: Optional[FhirList["CareTeamParticipantBackboneElement"]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[SNOMEDCTClinicalFindingsCode]]
        ] = None,
        reasonReference: Optional[FhirList[Reference["Condition"]]] = None,
        managingOrganization: Optional[FhirList[Reference[Organization]]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """
        CareTeam Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#CareTeam
        Planned participants in the coordination and delivery of care for a patient or group

        :param id_: id of resource
        :param identifier: External Ids for this team
        :param status: proposed | active | suspended | inactive | entered-in-error
        :param category: Type of team
        :param name: Name of the team, such as crisis assessment team
        :param subject: Who care team is for
        :param encounter: Encounter created as part of
        :param period: Time period team covers
        :param participant: Members of the team
                            + Rule: CareTeam.participant.onBehalfOf can only be populated when
                                    CareTeam.participant.member is a Practitioner
        :param reasonCode: Why the care team exists
        :param reasonReference: Why the care team exists
        :param managingOrganization: Organization responsible for the care team
        :param telecom: A contact detail for the care team (that applies to all members)
        :param note: Comments made about the CareTeam
        """
        super().__init__(
            resourceType="CareTeam",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            category=category,
            name=name,
            subject=subject,
            encounter=encounter,
            period=period,
            participant=participant,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            managingOrganization=managingOrganization,
            telecom=telecom,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CareTeamSchema.get_schema(include_extension=include_extension)
