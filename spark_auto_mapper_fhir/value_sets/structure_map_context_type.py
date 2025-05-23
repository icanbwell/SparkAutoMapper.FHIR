from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureMapContextTypeCode(GenericTypeCode):
    """
    StructureMapContextType
    From: http://hl7.org/fhir/map-context-type in valuesets.xml
        How to interpret the context.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/map-context-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/map-context-type"


class StructureMapContextTypeCodeValues:
    """
    The context specifies a type.
    From: http://hl7.org/fhir/map-context-type in valuesets.xml
    """

    Type = StructureMapContextTypeCode("type")
    """
    The context specifies a variable.
    From: http://hl7.org/fhir/map-context-type in valuesets.xml
    """
    Variable = StructureMapContextTypeCode("variable")
