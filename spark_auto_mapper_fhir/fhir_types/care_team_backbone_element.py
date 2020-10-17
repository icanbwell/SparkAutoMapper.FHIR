from typing import Union, Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.positive_int import AutoMapperFhirPositiveIntInputType
from spark_auto_mapper_fhir.fhir_types.practitioner import AutoMapperFhirDataTypePractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import AutoMapperFhirDataTypePractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class FhirCareTeamBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            sequence: AutoMapperFhirPositiveIntInputType,
            provider: AutoMapperFhirDataTypeReference[
                Union[
                    AutoMapperFhirDataTypePractitioner,
                    AutoMapperFhirDataTypePractitionerRole,
                    AutoMapperFhirDataTypeOrganization
                ]
            ],
            responsible: Optional[FhirBoolean] = None,
            role: Optional[AutoMapperFhirDataTypeCodeableConcept] = None,
            qualification: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'FhirCareTeamBackboneElement':
        """
        CareTeamBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.careTeam


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
