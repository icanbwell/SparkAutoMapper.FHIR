from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Encountertype(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class EncountertypeValues:
    AnnualDiabetesMellitusScreening = Encountertype("ADMS")
    BoneDrilling_boneMarrowPunctionInClinic = Encountertype("BD/BM-clin")
    InfantColonScreening_60Minutes = Encountertype("CCS60")
    OutpatientKenacortInjection = Encountertype("OKI")