from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AggregationModeCode(GenericTypeCode):
    """
    AggregationMode
    From: http://hl7.org/fhir/resource-aggregation-mode in valuesets.xml
        How resource references can be aggregated.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/resource-aggregation-mode
    """
    codeset: FhirUri = "http://hl7.org/fhir/resource-aggregation-mode"


class AggregationModeCodeValues:
    """
    The reference is a local reference to a contained resource.
    From: http://hl7.org/fhir/resource-aggregation-mode in valuesets.xml
    """

    Contained = AggregationModeCode("contained")
    """
    The reference to a resource that has to be resolved externally to the resource
    that includes the reference.
    From: http://hl7.org/fhir/resource-aggregation-mode in valuesets.xml
    """
    Referenced = AggregationModeCode("referenced")
