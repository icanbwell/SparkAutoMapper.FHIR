from typing import Union, Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.claim_care_team_role import FhirClaimCareTeamRoleCode
from spark_auto_mapper_fhir.fhir_types.valuesets.provider_qualification import FhirProviderQualificationCode
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirCareTeamBackboneElement(FhirResourceBase):
    @classmethod
    def map(
        cls,
        sequence: FhirPositiveInt,
        provider: FhirReference[Union[FhirPractitioner, FhirPractitionerRole,
                                      FhirOrganization]],
        responsible: Optional[FhirBoolean] = None,
        role: Optional[FhirCodeableConcept[FhirClaimCareTeamRoleCode]] = None,
        qualification: Optional[
            FhirCodeableConcept[FhirProviderQualificationCode]] = None
    ) -> 'FhirCareTeamBackboneElement':
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
        return FhirCareTeamBackboneElement(
            sequence=sequence,
            provider=provider,
            responsible=responsible,
            role=role,
            qualification=qualification
        )
