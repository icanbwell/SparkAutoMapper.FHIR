from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GoalLifecycleStatusCode(GenericTypeCode):
    """
    GoalLifecycleStatus
    From: http://hl7.org/fhir/goal-status in valuesets.xml
        Codes that reflect the current state of a goal and whether the goal is still
    being targeted.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/goal-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/goal-status"


class GoalLifecycleStatusCodeValues:
    """
    A goal is proposed for this patient.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """

    Proposed = GoalLifecycleStatusCode("proposed")
    """
    A goal is planned for this patient.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """
    Planned = GoalLifecycleStatusCode("planned")
    """
    A proposed goal was accepted or acknowledged.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """
    Accepted = GoalLifecycleStatusCode("accepted")
    """
    The goal has been abandoned.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """
    Cancelled = GoalLifecycleStatusCode("cancelled")
    """
    The goal was entered in error and voided.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """
    EnteredInError = GoalLifecycleStatusCode("entered-in-error")
    """
    A proposed goal was rejected.
    From: http://hl7.org/fhir/goal-status in valuesets.xml
    """
    Rejected = GoalLifecycleStatusCode("rejected")
