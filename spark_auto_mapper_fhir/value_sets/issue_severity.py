from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class IssueSeverityCode(GenericTypeCode):
    """
    IssueSeverity
    From: http://hl7.org/fhir/issue-severity in valuesets.xml
        How the issue affects the success of the action.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/issue-severity
    """
    codeset: FhirUri = "http://hl7.org/fhir/issue-severity"


class IssueSeverityCodeValues:
    """
    The issue caused the action to fail and no further checking could be
    performed.
    From: http://hl7.org/fhir/issue-severity in valuesets.xml
    """

    Fatal = IssueSeverityCode("fatal")
    """
    The issue is sufficiently important to cause the action to fail.
    From: http://hl7.org/fhir/issue-severity in valuesets.xml
    """
    Error = IssueSeverityCode("error")
    """
    The issue is not important enough to cause the action to fail but may cause it
    to be performed suboptimally or in a way that is not as desired.
    From: http://hl7.org/fhir/issue-severity in valuesets.xml
    """
    Warning = IssueSeverityCode("warning")
    """
    The issue has no relation to the degree of success of the action.
    From: http://hl7.org/fhir/issue-severity in valuesets.xml
    """
    Information = IssueSeverityCode("information")
