from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatementKindCode(GenericTypeCode):
    """
    CapabilityStatementKind
    From: http://hl7.org/fhir/capability-statement-kind in valuesets.xml
        How a capability statement is intended to be used.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/capability-statement-kind
    """
    codeset: FhirUri = "http://hl7.org/fhir/capability-statement-kind"


class CapabilityStatementKindCodeValues:
    """
    The CapabilityStatement instance represents the present capabilities of a
    specific system instance.  This is the kind returned by /metadata for a FHIR
    server end-point.
    From: http://hl7.org/fhir/capability-statement-kind in valuesets.xml
    """

    Instance = CapabilityStatementKindCode("instance")
    """
    The CapabilityStatement instance represents the capabilities of a system or
    piece of software, independent of a particular installation.
    From: http://hl7.org/fhir/capability-statement-kind in valuesets.xml
    """
    Capability = CapabilityStatementKindCode("capability")
    """
    The CapabilityStatement instance represents a set of requirements for other
    systems to meet; e.g. as part of an implementation guide or 'request for
    proposal'.
    From: http://hl7.org/fhir/capability-statement-kind in valuesets.xml
    """
    Requirements = CapabilityStatementKindCode("requirements")
