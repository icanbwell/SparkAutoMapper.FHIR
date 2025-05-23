from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GoalStatusReasonCode(GenericTypeCode):
    """
    GoalStatusReason
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
        Example codes indicating the reason for a current status.  Note that these are
    in no way complete and might not even be appropriate for some uses.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/goal-status-reason
    """
    codeset: FhirUri = "http://hl7.org/fhir/goal-status-reason"


class GoalStatusReasonCodeValues:
    """
    Goal suspended or ended because of a surgical procedure.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """

    Surgery = GoalStatusReasonCode("surgery")
    """
    Goal suspended or ended because of a significant life event (marital change,
    bereavement, etc.).
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    LifeEvent = GoalStatusReasonCode("life-event")
    """
    Goal has been superseded by a new goal.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    Replaced = GoalStatusReasonCode("replaced")
    """
    Patient wishes the goal to be set aside, at least temporarily.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    PatientRequest = GoalStatusReasonCode("patient-request")
    """
    Goal cannot be reached temporarily.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    GoalNotAttainableTemporarily = GoalStatusReasonCode("temp-not-attainable")
    """
    Goal cannot be reached permanently.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    GoalNotAttainablePermanently = GoalStatusReasonCode("permanent-not-attainable")
    """
    Goal cannot be reached due to financial barrier or reason.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    FinancialReason = GoalStatusReasonCode("financial-barrier")
    """
    Goal cannot be reached due to a lack of transportation.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    LackOfTransportation = GoalStatusReasonCode("lack-of-transportation")
    """
    Goal cannot be reached due to a lack of social support.
    From: http://hl7.org/fhir/goal-status-reason in valuesets.xml
    """
    LackOfSocialSupport = GoalStatusReasonCode("lack-of-social-support")
