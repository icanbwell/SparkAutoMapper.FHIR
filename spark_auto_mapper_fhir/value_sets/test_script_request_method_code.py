from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptRequestMethodCode(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class TestScriptRequestMethodCodeValues:
    DELETE = TestScriptRequestMethodCode("delete")
    GET = TestScriptRequestMethodCode("get")
    OPTIONS = TestScriptRequestMethodCode("options")
    PATCH = TestScriptRequestMethodCode("patch")
    POST = TestScriptRequestMethodCode("post")
    PUT = TestScriptRequestMethodCode("put")
    HEAD = TestScriptRequestMethodCode("head")