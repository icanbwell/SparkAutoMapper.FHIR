from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Specialcourtesy(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class SpecialcourtesyValues:
    ExtendedCourtesy = Specialcourtesy("EXT")
    NormalCourtesy = Specialcourtesy("NRM")
    ProfessionalCourtesy = Specialcourtesy("PRF")
    Staff = Specialcourtesy("STF")
    VeryImportantPerson = Specialcourtesy("VIP")
    Ext = Specialcourtesy("EXT")
    Nrm = Specialcourtesy("NRM")
    Prf = Specialcourtesy("PRF")
    Stf = Specialcourtesy("STF")
    Vip = Specialcourtesy("VIP")
    Noinformation = Specialcourtesy("NI")
    NotPresent = Specialcourtesy("NP")
    Unk = Specialcourtesy("UNK")