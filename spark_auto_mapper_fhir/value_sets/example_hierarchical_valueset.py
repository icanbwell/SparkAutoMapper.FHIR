from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleHierarchicalValueset(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ExampleHierarchicalValuesetValues:
    Invalid = ExampleHierarchicalValueset("invalid")
    Structure = ExampleHierarchicalValueset("structure")
    Required = ExampleHierarchicalValueset("required")
    Value = ExampleHierarchicalValueset("value")
    Processing = ExampleHierarchicalValueset("processing")
    Duplicate = ExampleHierarchicalValueset("duplicate")
    Not_found = ExampleHierarchicalValueset("not-found")
    Conflict = ExampleHierarchicalValueset("conflict")
    Lock = ExampleHierarchicalValueset("lock")
    Exception = ExampleHierarchicalValueset("exception")
    Tbrottled = ExampleHierarchicalValueset("tbrottled")
    Login = ExampleHierarchicalValueset("login")
    Unknown = ExampleHierarchicalValueset("unknown")