from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FamilyHistoryAbsentReasonCode(GenericTypeCode):
    """
    FamilyHistoryAbsentReason
    From: http://terminology.hl7.org/CodeSystem/history-absent-reason in valuesets.xml
        Codes describing the reason why a family member's history is not available.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/history-absent-reason
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/history-absent-reason"


class FamilyHistoryAbsentReasonCodeValues:
    """
    Patient does not know the subject, e.g. the biological parent of an adopted
    patient.
    From: http://terminology.hl7.org/CodeSystem/history-absent-reason in valuesets.xml
    """

    SubjectUnknown = FamilyHistoryAbsentReasonCode("subject-unknown")
    """
    The patient withheld or refused to share the information.
    From: http://terminology.hl7.org/CodeSystem/history-absent-reason in valuesets.xml
    """
    InformationWithheld = FamilyHistoryAbsentReasonCode("withheld")
    """
    Information cannot be obtained; e.g. unconscious patient.
    From: http://terminology.hl7.org/CodeSystem/history-absent-reason in valuesets.xml
    """
    UnableToObtain = FamilyHistoryAbsentReasonCode("unable-to-obtain")
    """
    Patient does not have the information now, but can provide the information at
    a later date.
    From: http://terminology.hl7.org/CodeSystem/history-absent-reason in valuesets.xml
    """
    Deferred = FamilyHistoryAbsentReasonCode("deferred")
