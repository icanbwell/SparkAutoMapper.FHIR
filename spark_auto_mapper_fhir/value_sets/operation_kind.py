from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OperationKindCode(GenericTypeCode):
    """
    OperationKind
    From: http://hl7.org/fhir/operation-kind in valuesets.xml
        Whether an operation is a normal operation or a query.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/operation-kind
    """
    codeset: FhirUri = "http://hl7.org/fhir/operation-kind"


class OperationKindCodeValues:
    """
    This operation is invoked as an operation.
    From: http://hl7.org/fhir/operation-kind in valuesets.xml
    """

    Operation = OperationKindCode("operation")
    """
    This operation is a named query, invoked using the search mechanism.
    From: http://hl7.org/fhir/operation-kind in valuesets.xml
    """
    Query = OperationKindCode("query")
