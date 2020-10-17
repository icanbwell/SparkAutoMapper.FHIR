from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept


class FhirSubstitutionBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            allowedBoolean: Optional[FhirBoolean] = None,
            allowedCodeableConcept: Optional[FhirCodeableConcept] = None,
            reason: Optional[FhirCodeableConcept] = None
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
