from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Identityassurancelevel(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class IdentityassurancelevelValues:
    Level1 = Identityassurancelevel("level1")
    Level2 = Identityassurancelevel("level2")
    Level3 = Identityassurancelevel("level3")
    Level4 = Identityassurancelevel("level4")