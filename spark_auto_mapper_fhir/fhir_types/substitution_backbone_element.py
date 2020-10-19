from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.act_substance_admin_substitution_code import \
    FhirActSubstanceAdminSubstitutionCode
from spark_auto_mapper_fhir.fhir_types.valuesets.substance_admin_substitution_reason import \
    FhirSubstanceAdminSubstitutionReason


class FhirSubstitutionBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(
        cls,
        allowedBoolean: Optional[FhirBoolean] = None,
        allowedCodeableConcept: Optional[
            FhirCodeableConcept[FhirActSubstanceAdminSubstitutionCode]] = None,
        reason: Optional[
            FhirCodeableConcept[FhirSubstanceAdminSubstitutionReason]] = None
    ) -> 'FhirSubstitutionBackboneElement':
        """
        SubstitutionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SubstitutionBackboneElement


        :param allowedBoolean: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param allowedCodeableConcept: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param reason: Why should (not) substitution be made. https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
        """
        return FhirSubstitutionBackboneElement(
            allowedBoolean=allowedBoolean,
            allowedCodeableConcept=allowedCodeableConcept,
            reason=reason
        )
