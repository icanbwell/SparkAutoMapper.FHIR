from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProvenanceHistoryRecordActivityCodesCode(GenericTypeCode):
    """
    ProvenanceHistoryRecordActivityCodes
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
        Codes for Provenance activities that are relevant when capturing event history
    for resources.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-DataOperation
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-DataOperation"


class ProvenanceHistoryRecordActivityCodesCodeValues:
    """
    Description:Act on an object or objects.
    From: http://terminology.hl7.org/CodeSystem/v3-DataOperation in v3-codesystems.xml
    """

    Operate = ProvenanceHistoryRecordActivityCodesCode("OPERATE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Created = ProvenanceHistoryRecordActivityCodesCode("CREATE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Updated = ProvenanceHistoryRecordActivityCodesCode("UPDATE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Deleted = ProvenanceHistoryRecordActivityCodesCode("DELETE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Stopped_Ended_Aborted = ProvenanceHistoryRecordActivityCodesCode("ABORT")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Held = ProvenanceHistoryRecordActivityCodesCode("HOLD")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Released = ProvenanceHistoryRecordActivityCodesCode("RELEASE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Cancelled = ProvenanceHistoryRecordActivityCodesCode("CANCEL")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Activated = ProvenanceHistoryRecordActivityCodesCode("ACTIVATE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Suspended = ProvenanceHistoryRecordActivityCodesCode("SUSPEND")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    RESUME = ProvenanceHistoryRecordActivityCodesCode("RESUME")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Completed = ProvenanceHistoryRecordActivityCodesCode("COMPLETE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    MarkEntered_in_error = ProvenanceHistoryRecordActivityCodesCode("NULLIFY")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Replaced = ProvenanceHistoryRecordActivityCodesCode("OBSOLETE")
    """
    From: http://hl7.org/fhir/ValueSet/provenance-history-record-activity in valuesets.xml
    """
    Reactivated = ProvenanceHistoryRecordActivityCodesCode("REACTIVATE")
