from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleHierarchicalValueSet(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ExampleHierarchicalValueSetValues:
    Invalid = ExampleHierarchicalValueSet("invalid")
    Structure = ExampleHierarchicalValueSet("structure")
    Required = ExampleHierarchicalValueSet("required")
    Value = ExampleHierarchicalValueSet("value")
    Processing = ExampleHierarchicalValueSet("processing")
    Duplicate = ExampleHierarchicalValueSet("duplicate")
    Not_found = ExampleHierarchicalValueSet("not-found")
    Conflict = ExampleHierarchicalValueSet("conflict")
    Lock = ExampleHierarchicalValueSet("lock")
    Exception = ExampleHierarchicalValueSet("exception")
    Tbrottled = ExampleHierarchicalValueSet("tbrottled")
    Login = ExampleHierarchicalValueSet("login")
    Unknown = ExampleHierarchicalValueSet("unknown")