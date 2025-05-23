from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActRelationshipCheckpoint(GenericTypeCode):
    """
    v3.ActRelationshipCheckpoint
    From: http://terminology.hl7.org/ValueSet/v3-ActRelationshipCheckpoint in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint"
    )


class ActRelationshipCheckpointValues:
    """
    Condition is tested every time before execution of the service (WHILE
    condition DO service).
    From: http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint in v3-codesystems.xml
    """

    Beginning = ActRelationshipCheckpoint("B")
    """
    Condition is tested at the end of a repeated service execution.  The service
    is repeated only if the condition is true (DO service WHILE condition).
    From: http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint in v3-codesystems.xml
    """
    End = ActRelationshipCheckpoint("E")
    """
    Condition is tested once before the service is executed (IF condition THEN
    service).
    From: http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint in v3-codesystems.xml
    """
    Entry = ActRelationshipCheckpoint("S")
    """
    Condition must be true throughout the execution and the service is interrupted
    (asynchronously) as soon as the condition turns false (asynchronous WHILE
    loop).  The service must be interruptible.
    From: http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint in v3-codesystems.xml
    """
    Through = ActRelationshipCheckpoint("T")
    """
    Condition is a loop checkpoint, i.e. it is a step of an activity plan and, if
    negative causes the containing loop to exit.
    From: http://terminology.hl7.org/CodeSystem/v3-ActRelationshipCheckpoint in v3-codesystems.xml
    """
    Exit = ActRelationshipCheckpoint("X")
