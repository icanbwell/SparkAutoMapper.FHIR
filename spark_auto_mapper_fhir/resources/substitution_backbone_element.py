from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.act_substance_admin_substitution_code import \
    ActSubstanceAdminSubstitutionCode
from spark_auto_mapper_fhir.valuesets.substance_admin_substitution_reason import \
    SubstanceAdminSubstitutionReason


class SubstitutionBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        allowedBoolean: Optional[FhirBoolean] = None,
        allowedCodeableConcept: Optional[
            CodeableConcept[ActSubstanceAdminSubstitutionCode]] = None,
        reason: Optional[CodeableConcept[SubstanceAdminSubstitutionReason]
                         ] = None
    ):
        """
        SubstitutionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SubstitutionBackboneElement


        :param allowedBoolean: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param allowedCodeableConcept: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param reason: Why should (not) substitution be made. https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
        """
        super().__init__(
            allowedBoolean=allowedBoolean,
            allowedCodeableConcept=allowedCodeableConcept,
            reason=reason
        )
