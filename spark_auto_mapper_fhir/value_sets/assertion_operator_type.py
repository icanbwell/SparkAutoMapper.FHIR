from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AssertionOperatorType(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class AssertionOperatorTypeValues:
    Equals = AssertionOperatorType("equals")
    NotEquals = AssertionOperatorType("notEquals")
    In = AssertionOperatorType("in")
    NotIn = AssertionOperatorType("notIn")
    GreaterThan = AssertionOperatorType("greaterThan")
    LessThan = AssertionOperatorType("lessThan")
    Empty = AssertionOperatorType("empty")
    NotEmpty = AssertionOperatorType("notEmpty")
    Contains = AssertionOperatorType("contains")
    NotContains = AssertionOperatorType("notContains")
    Evaluate = AssertionOperatorType("eval")