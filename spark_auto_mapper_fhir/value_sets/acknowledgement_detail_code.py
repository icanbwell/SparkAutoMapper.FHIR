from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AcknowledgementDetailCode(GenericTypeCode):
    """
    v3.AcknowledgementDetailCode
    From: http://terminology.hl7.org/ValueSet/v3-AcknowledgementDetailCode in v3-codesystems.xml
          OpenIssue:
    Missing description.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode"
    )


class AcknowledgementDetailCodeValues:
    """
    Refelects rejections because elements of the communication are not supported
    in the current context.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """

    AcknowledgementDetailNotSupportedCode = AcknowledgementDetailCode(
        "_AcknowledgementDetailNotSupportedCode"
    )
    """
    An internal software component (database, application, queue mechanism, etc.)
    has failed, leading to inability to process the message.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    InternalSystemError = AcknowledgementDetailCode("INTERR")
    """
    Rejection: The message can't be stored by the receiver due to an unspecified
    internal application issue. The message was neither processed nor stored by
    the receiving application.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    NoStorageSpaceForMessage_ = AcknowledgementDetailCode("NOSTORE")
    """
    Error: The destination of this message is known to the receiving application.
    Messages have been successfully routed to that destination in the past. The
    link to the destination application or an intermediate application is
    unavailable.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    MessageRoutingError_DestinationUnreachable_ = AcknowledgementDetailCode("RTEDEST")
    """
    The destination of this message is unknown to the receiving application. The
    receiving application in the message does not match the application which
    received the message. The message was neither routed, processed nor stored by
    the receiving application.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    Error_MessageRoutingError_UnknownDestination_ = AcknowledgementDetailCode("RTUDEST")
    """
    Warning: The destination of this message is known to the receiving
    application. Messages have been successfully routed to that destination in the
    past. The link to the destination application or an intermediate application
    is (temporarily) unavailable. The receiving application will forward the
    message as soon as the destination can be reached again.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    MessageRoutingWarning_DestinationUnreachable_ = AcknowledgementDetailCode("RTWDEST")
    """
    Reflects errors in the syntax or structure of the communication.
    From: http://terminology.hl7.org/CodeSystem/v3-AcknowledgementDetailCode in v3-codesystems.xml
    """
    SyntaxError = AcknowledgementDetailCode("SYN")
