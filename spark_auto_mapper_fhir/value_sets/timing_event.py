from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TimingEvent(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class TimingEventValues:
    Ac = TimingEvent("AC")
    Acd = TimingEvent("ACD")
    Acm = TimingEvent("ACM")
    Acv = TimingEvent("ACV")
    C = TimingEvent("C")
    Hs = TimingEvent("HS")
    Ic = TimingEvent("IC")
    Icd = TimingEvent("ICD")
    Icm = TimingEvent("ICM")
    Icv = TimingEvent("ICV")
    Pc = TimingEvent("PC")
    Pcd = TimingEvent("PCD")
    Pcm = TimingEvent("PCM")
    Pcv = TimingEvent("PCV")
    Wake = TimingEvent("WAKE")