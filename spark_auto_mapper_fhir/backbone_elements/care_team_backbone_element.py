from typing import Union, Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.claim_care_team_role import ClaimCareTeamRoleCode
from spark_auto_mapper_fhir.valuesets.provider_qualification import (
    ProviderQualificationCode,
)
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.complex_types.reference import Reference


class CareTeamBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        sequence: FhirPositiveInt,
        provider: Reference[Union[Practitioner, PractitionerRole, Organization]],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        responsible: Optional[FhirBoolean] = None,
        role: Optional[CodeableConcept[ClaimCareTeamRoleCode]] = None,
        qualification: Optional[CodeableConcept[ProviderQualificationCode]] = None,
    ):
        """
        CareTeamBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.careTeam
        The members of the team who provided the products and services.

        :param sequence: Order of care team
        :param provider: Practitioner or organization
        :param responsible: Indicator of the lead practitioner
        :param role: Function within the team. https://hl7.org/FHIR/valueset-claim-careteamrole.html
        :param qualification: Practitioner credential or specialization. https://hl7.org/FHIR/valueset-provider-qualification.html
        """
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            provider=provider,
            responsible=responsible,
            role=role,
            qualification=qualification,
        )
