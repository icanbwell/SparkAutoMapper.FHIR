from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InsurancePlanTypeCode(GenericTypeCode):
    """
    InsurancePlanType
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
        This example value set defines a set of codes that can be used to indicate a
    type of insurance plan.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/insurance-plan-type
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/insurance-plan-type"


class InsurancePlanTypeCodeValues:
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """

    Medical = InsurancePlanTypeCode("medical")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    Dental = InsurancePlanTypeCode("dental")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    MentalHealth = InsurancePlanTypeCode("mental")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    SubstanceAbuse = InsurancePlanTypeCode("subst-ab")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    Vision = InsurancePlanTypeCode("vision")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    Drug = InsurancePlanTypeCode("Drug")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    ShortTerm = InsurancePlanTypeCode("short-term")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    LongTermCare = InsurancePlanTypeCode("long-term")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    Hospice = InsurancePlanTypeCode("hospice")
    """
    From: http://terminology.hl7.org/CodeSystem/insurance-plan-type in valuesets.xml
    """
    HomeHealth = InsurancePlanTypeCode("home")
