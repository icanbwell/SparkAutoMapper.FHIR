from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RestfulCapabilityModeCode(GenericTypeCode):
    """
    RestfulCapabilityMode
    From: http://hl7.org/fhir/restful-capability-mode in valuesets.xml
        The mode of a RESTful capability statement.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/restful-capability-mode
    """
    codeset: FhirUri = "http://hl7.org/fhir/restful-capability-mode"


class RestfulCapabilityModeCodeValues:
    """
    The application acts as a client for this resource.
    From: http://hl7.org/fhir/restful-capability-mode in valuesets.xml
    """

    Client = RestfulCapabilityModeCode("client")
    """
    The application acts as a server for this resource.
    From: http://hl7.org/fhir/restful-capability-mode in valuesets.xml
    """
    Server = RestfulCapabilityModeCode("server")
