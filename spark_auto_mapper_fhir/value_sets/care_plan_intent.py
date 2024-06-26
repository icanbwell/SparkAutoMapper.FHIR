from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CarePlanIntentCode(GenericTypeCode):
    """
    CarePlanIntent
    From: http://hl7.org/fhir/ValueSet/care-plan-intent in valuesets.xml
        Codes indicating the degree of authority/intentionality associated with a care
    plan.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/request-intent
    """
    codeset: FhirUri = "http://hl7.org/fhir/request-intent"


class CarePlanIntentCodeValues:
    """
    From: http://hl7.org/fhir/ValueSet/care-plan-intent in valuesets.xml
    """

    Proposal = CarePlanIntentCode("proposal")
    """
    From: http://hl7.org/fhir/ValueSet/care-plan-intent in valuesets.xml
    """
    Plan = CarePlanIntentCode("plan")
    """
    From: http://hl7.org/fhir/ValueSet/care-plan-intent in valuesets.xml
    """
    Order = CarePlanIntentCode("order")
    """
    From: http://hl7.org/fhir/ValueSet/care-plan-intent in valuesets.xml
    """
    Option = CarePlanIntentCode("option")
