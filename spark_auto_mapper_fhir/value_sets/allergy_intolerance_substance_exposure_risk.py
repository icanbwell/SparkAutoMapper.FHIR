from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AllergyIntoleranceSubstanceExposureRiskCode(GenericTypeCode):
    """
    AllergyIntoleranceSubstanceExposureRisk
    From: http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk in valuesets.xml
        The risk of an adverse reaction (allergy or intolerance) for this patient upon
    exposure to the substance (including pharmaceutical products).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk"
    )


class AllergyIntoleranceSubstanceExposureRiskCodeValues:
    """
    Known risk of allergy or intolerance reaction upon exposure to the specified
    substance.
    From: http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk in valuesets.xml
    """

    KnownReactionRisk = AllergyIntoleranceSubstanceExposureRiskCode(
        "known-reaction-risk"
    )
    """
    No known risk of allergy or intolerance reaction upon exposure to the
    specified substance.
    From: http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk in valuesets.xml
    """
    NoKnownReactionRisk = AllergyIntoleranceSubstanceExposureRiskCode(
        "no-known-reaction-risk"
    )
