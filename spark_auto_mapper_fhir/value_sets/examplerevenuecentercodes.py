from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Examplerevenuecentercodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ExamplerevenuecentercodesValues:
    Anaesthesia = Examplerevenuecentercodes("0370")
    PhysicalTherapy = Examplerevenuecentercodes("0420")
    PhysicalTherapy_ = Examplerevenuecentercodes("0421")
    Speech_languagePathology = Examplerevenuecentercodes("0440")
    Speech_languagePathology_Visit = Examplerevenuecentercodes("0441")
    EmergencyRoom = Examplerevenuecentercodes("0450")
    EmergencyRoom_Em_emtala = Examplerevenuecentercodes("0451")
    EmergencyRoom_BeyondEmtala = Examplerevenuecentercodes("0452")
    VisionClinic = Examplerevenuecentercodes("0010")