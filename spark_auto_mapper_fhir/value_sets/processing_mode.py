from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProcessingMode(GenericTypeCode):
    """
    v3.ProcessingMode
    From: http://terminology.hl7.org/ValueSet/v3-ProcessingMode in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ProcessingMode
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ProcessingMode"


class ProcessingModeValues:
    """
    Identifies archive mode of processing.
    From: http://terminology.hl7.org/CodeSystem/v3-ProcessingMode in v3-codesystems.xml
    """

    Archive = ProcessingMode("A")
    """
    Identifies initial load mode of processing.
    From: http://terminology.hl7.org/CodeSystem/v3-ProcessingMode in v3-codesystems.xml
    """
    InitialLoad = ProcessingMode("I")
    """
    Identifies restore mode of processing.
    From: http://terminology.hl7.org/CodeSystem/v3-ProcessingMode in v3-codesystems.xml
    """
    RestoreFromArchive = ProcessingMode("R")
    """
    Identifies on-line mode of processing.
    From: http://terminology.hl7.org/CodeSystem/v3-ProcessingMode in v3-codesystems.xml
    """
    CurrentProcessing = ProcessingMode("T")
