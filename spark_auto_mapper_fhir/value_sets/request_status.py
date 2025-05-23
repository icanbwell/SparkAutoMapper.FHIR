from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RequestStatusCode(GenericTypeCode):
    """
    RequestStatus
    From: http://hl7.org/fhir/request-status in valuesets.xml
        Codes identifying the lifecycle stage of a request.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/request-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/request-status"


class RequestStatusCodeValues:
    """
    The request has been created but is not yet complete or ready for action.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """

    Draft = RequestStatusCode("draft")
    """
    The request is in force and ready to be acted upon.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    Active = RequestStatusCode("active")
    """
    The request (and any implicit authorization to act) has been temporarily
    withdrawn but is expected to resume in the future.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    OnHold = RequestStatusCode("on-hold")
    """
    The request (and any implicit authorization to act) has been terminated prior
    to the known full completion of the intended actions.  No further activity
    should occur.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    Revoked = RequestStatusCode("revoked")
    """
    The activity described by the request has been fully performed.  No further
    activity will occur.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    Completed = RequestStatusCode("completed")
    """
    This request should never have existed and should be considered 'void'.  (It
    is possible that real-world decisions were based on it.  If real-world
    activity has occurred, the status should be "revoked" rather than "entered-in-
    error".).
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    EnteredInError = RequestStatusCode("entered-in-error")
    """
    The authoring/source system does not know which of the status values currently
    applies for this request.  Note: This concept is not to be used for "other" -
    one of the listed statuses is presumed to apply,  but the authoring/source
    system does not know which.
    From: http://hl7.org/fhir/request-status in valuesets.xml
    """
    Unknown = RequestStatusCode("unknown")
