from typing import Union, Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperBooleanInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept


class FhirSubstitutionBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            allowed: Optional[Union[AutoMapperBooleanInputType, FhirCodeableConcept]] = None,
            reason: Optional[FhirCodeableConcept] = None
            ) -> 'FhirSubstitutionBackboneElement':
        """
        SubstitutionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SubstitutionBackboneElement


        :param allowed: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param reason: Why should (not) substitution be made. https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
        """
        return FhirSubstitutionBackboneElement(
            allowed=allowed,
            reason=reason
        )
