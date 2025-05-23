from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DataOperation(GenericTypeCode):
    """
    v3.DataOperation
    From: http://terminology.hl7.org/ValueSet/v3-DataOperation in v3-codesystems.xml
        **** MISSING DEFINITIONS ****
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-DataOperation
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-DataOperation"


class DataOperationValues:
    """
    Description:Act on an object or objects.
    From: http://terminology.hl7.org/CodeSystem/v3-DataOperation in v3-codesystems.xml
    """

    Operate = DataOperation("OPERATE")
