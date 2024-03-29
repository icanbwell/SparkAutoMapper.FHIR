from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StatusCode(GenericTypeCode):
    """
    status
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
        The validation status of the target
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/CodeSystem/status
    """
    codeset: FhirUri = "http://hl7.org/fhir/CodeSystem/status"


class StatusCodeValues:
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """

    Attested = StatusCode("attested")
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """
    Validated = StatusCode("validated")
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """
    InProcess = StatusCode("in-process")
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """
    RequiresRevalidation = StatusCode("req-revalid")
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """
    ValidationFailed = StatusCode("val-fail")
    """
    ***TODO***
    From: http://hl7.org/fhir/CodeSystem/status in valuesets.xml
    """
    Re_ValidationFailed = StatusCode("reval-fail")
