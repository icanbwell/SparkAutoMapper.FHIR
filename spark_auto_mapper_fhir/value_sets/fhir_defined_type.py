from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FHIRDefinedTypeCode(GenericTypeCode):
    """
    FHIRDefinedType
    From: http://hl7.org/fhir/ValueSet/defined-types in valuesets.xml
        A list of all the concrete types defined in this version of the FHIR
    specification - Data Types and Resource Types.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/data-types
    """
    codeset_data_types: FhirUri = "http://hl7.org/fhir/data-types"
    """
    http://hl7.org/fhir/resource-types
    """
    codeset_resource_types: FhirUri = "http://hl7.org/fhir/resource-types"
