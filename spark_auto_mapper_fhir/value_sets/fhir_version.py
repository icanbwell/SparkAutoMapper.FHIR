from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FHIRVersion(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class FHIRVersionValues:
    _0_01 = FHIRVersion("0.01")
    _0_05 = FHIRVersion("0.05")
    _0_06 = FHIRVersion("0.06")
    _0_11 = FHIRVersion("0.11")
    _0_0_80 = FHIRVersion("0.0.80")
    _0_0_81 = FHIRVersion("0.0.81")
    _0_0_82 = FHIRVersion("0.0.82")
    _0_4_0 = FHIRVersion("0.4.0")
    _0_5_0 = FHIRVersion("0.5.0")
    _1_0_0 = FHIRVersion("1.0.0")
    _1_0_1 = FHIRVersion("1.0.1")
    _1_0_2 = FHIRVersion("1.0.2")
    _1_1_0 = FHIRVersion("1.1.0")
    _1_4_0 = FHIRVersion("1.4.0")
    _1_6_0 = FHIRVersion("1.6.0")
    _1_8_0 = FHIRVersion("1.8.0")
    _3_0_0 = FHIRVersion("3.0.0")
    _3_0_1 = FHIRVersion("3.0.1")
    _3_3_0 = FHIRVersion("3.3.0")
    _3_5_0 = FHIRVersion("3.5.0")
    _4_0_0 = FHIRVersion("4.0.0")
    _4_0_1 = FHIRVersion("4.0.1")