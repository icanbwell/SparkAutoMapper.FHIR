from typing import Union, Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperBooleanInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept


class AutoMapperFhirDataTypeSubstitutionBackboneElement(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            allowed: Optional[Union[AutoMapperBooleanInputType, AutoMapperFhirDataTypeCodeableConcept]] = None,
            reason: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'AutoMapperFhirDataTypeSubstitutionBackboneElement':
        """
        SubstitutionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SubstitutionBackboneElement


        :param allowed: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param reason: Why should (not) substitution be made. https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
        """
        return AutoMapperFhirDataTypeSubstitutionBackboneElement(
            allowed=allowed,
            reason=reason
        )
