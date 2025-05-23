from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationReasonCodesCode(GenericTypeCode):
    """
    ImmunizationReasonCodes
    From: http://hl7.org/fhir/ValueSet/immunization-reason in valuesets.xml
        The value set to instantiate this attribute should be drawn from a
    terminologically robust code system that consists of or contains concepts to
    support describing the reason why a dose of vaccine was administered. This
    value set is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://snomed.info/sct
    """
    codeset: FhirUri = "http://snomed.info/sct"


class ImmunizationReasonCodesCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/immunization-reason in valuesets.xml
    """

    _429060002 = ImmunizationReasonCodesCode("429060002")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-reason in valuesets.xml
    """
    _281657000 = ImmunizationReasonCodesCode("281657000")
