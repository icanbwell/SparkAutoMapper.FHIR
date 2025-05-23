from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EventCapabilityModeCode(GenericTypeCode):
    """
    EventCapabilityMode
    From: http://hl7.org/fhir/event-capability-mode in valuesets.xml
        The mode of a message capability statement.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/event-capability-mode
    """
    codeset: FhirUri = "http://hl7.org/fhir/event-capability-mode"


class EventCapabilityModeCodeValues:
    """
    The application sends requests and receives responses.
    From: http://hl7.org/fhir/event-capability-mode in valuesets.xml
    """

    Sender = EventCapabilityModeCode("sender")
    """
    The application receives requests and sends responses.
    From: http://hl7.org/fhir/event-capability-mode in valuesets.xml
    """
    Receiver = EventCapabilityModeCode("receiver")
