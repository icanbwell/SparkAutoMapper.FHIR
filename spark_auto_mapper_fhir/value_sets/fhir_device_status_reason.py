from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FHIRDeviceStatusReason(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class FHIRDeviceStatusReasonValues:
    Online = FHIRDeviceStatusReason("online")
    Paused = FHIRDeviceStatusReason("paused")
    Standby = FHIRDeviceStatusReason("standby")
    Offline = FHIRDeviceStatusReason("offline")
    NotReady = FHIRDeviceStatusReason("not-ready")
    TransducerDisconnected = FHIRDeviceStatusReason("transduc-discon")
    HardwareDisconnected = FHIRDeviceStatusReason("hw-discon")
    Off = FHIRDeviceStatusReason("off")