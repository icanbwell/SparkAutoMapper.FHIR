from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MeasureTypeCode(GenericTypeCode):
    """
    MeasureType
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
        The type of measure (includes codes from 2.16.840.1.113883.1.11.20368).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/measure-type
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/measure-type"


class MeasureTypeCodeValues:
    """
    A measure which focuses on a process which leads to a certain outcome, meaning
    that a scientific basis exists for believing that the process, when executed
    well, will increase the probability of achieving a desired outcome.
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
    """

    Process = MeasureTypeCode("process")
    """
    A measure that indicates the result of the performance (or non-performance) of
    a function or process.
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
    """
    Outcome = MeasureTypeCode("outcome")
    """
    A measure that focuses on a health care provider's capacity, systems, and
    processes to provide high-quality care.
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
    """
    Structure = MeasureTypeCode("structure")
    """
    A measure that focuses on patient-reported information such as patient
    engagement or patient experience measures.
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
    """
    PatientReportedOutcome = MeasureTypeCode("patient-reported-outcome")
    """
    A measure that combines multiple component measures in to a single quality
    measure.
    From: http://terminology.hl7.org/CodeSystem/measure-type in valuesets.xml
    """
    Composite = MeasureTypeCode("composite")
