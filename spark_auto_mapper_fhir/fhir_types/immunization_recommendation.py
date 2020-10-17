from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirImmunizationRecommendation(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            ) -> 'FhirImmunizationRecommendation':
        """
        ImmunizationRecommendation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ImmunizationRecommendation
        """
        return FhirImmunizationRecommendation(
        )
