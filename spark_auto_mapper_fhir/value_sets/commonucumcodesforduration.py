from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Commonucumcodesforduration(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class CommonucumcodesfordurationValues:
    Milliseconds = Commonucumcodesforduration("ms")
    Seconds = Commonucumcodesforduration("s")
    Minutes = Commonucumcodesforduration("min")
    Hours = Commonucumcodesforduration("h")
    Days = Commonucumcodesforduration("d")
    Weeks = Commonucumcodesforduration("wk")
    Months = Commonucumcodesforduration("mo")
    Years = Commonucumcodesforduration("a")