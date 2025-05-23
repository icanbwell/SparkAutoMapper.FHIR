from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EvidenceVariantStateCode(GenericTypeCode):
    """
    EvidenceVariantState
    From: http://terminology.hl7.org/CodeSystem/evidence-variant-state in valuesets.xml
        Used for results by exposure in variant states such as low-risk, medium-risk
    and high-risk states.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/evidence-variant-state
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/evidence-variant-state"


class EvidenceVariantStateCodeValues:
    """
    low risk estimate.
    From: http://terminology.hl7.org/CodeSystem/evidence-variant-state in valuesets.xml
    """

    LowRisk = EvidenceVariantStateCode("low-risk")
    """
    medium risk estimate.
    From: http://terminology.hl7.org/CodeSystem/evidence-variant-state in valuesets.xml
    """
    MediumRisk = EvidenceVariantStateCode("medium-risk")
    """
    high risk estimate.
    From: http://terminology.hl7.org/CodeSystem/evidence-variant-state in valuesets.xml
    """
    HighRisk = EvidenceVariantStateCode("high-risk")
