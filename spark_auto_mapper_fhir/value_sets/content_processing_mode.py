from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContentProcessingMode(GenericTypeCode):
    """
    v3.ContentProcessingMode
    From: http://terminology.hl7.org/ValueSet/v3-ContentProcessingMode in v3-codesystems.xml
          Description:
    Identifies the order in which content should be processed.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ContentProcessingMode
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ContentProcessingMode"


class ContentProcessingModeValues:
    """
    Description:The content should be processed in a sequential fashion.
    From: http://terminology.hl7.org/CodeSystem/v3-ContentProcessingMode in v3-codesystems.xml
    """

    Sequential = ContentProcessingMode("SEQL")
    """
    Description:The content may be processed in any order.
    From: http://terminology.hl7.org/CodeSystem/v3-ContentProcessingMode in v3-codesystems.xml
    """
    Unordered = ContentProcessingMode("UNOR")
