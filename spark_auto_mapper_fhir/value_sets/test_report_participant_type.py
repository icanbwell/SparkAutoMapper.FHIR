from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestReportParticipantTypeCode(GenericTypeCode):
    """
    TestReportParticipantType
    From: http://hl7.org/fhir/report-participant-type in valuesets.xml
        The type of participant.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/report-participant-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/report-participant-type"


class TestReportParticipantTypeCodeValues:
    """
    The test execution engine.
    From: http://hl7.org/fhir/report-participant-type in valuesets.xml
    """

    TestEngine = TestReportParticipantTypeCode("test-engine")
    """
    A FHIR Client.
    From: http://hl7.org/fhir/report-participant-type in valuesets.xml
    """
    Client = TestReportParticipantTypeCode("client")
    """
    A FHIR Server.
    From: http://hl7.org/fhir/report-participant-type in valuesets.xml
    """
    Server = TestReportParticipantTypeCode("server")
