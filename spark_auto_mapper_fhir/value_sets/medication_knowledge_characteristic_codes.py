from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledgeCharacteristicCodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class MedicationKnowledgeCharacteristicCodesValues:
    ImprintCode = MedicationKnowledgeCharacteristicCodes("imprintcd")
    Size = MedicationKnowledgeCharacteristicCodes("size")
    Shape = MedicationKnowledgeCharacteristicCodes("shape")
    Color = MedicationKnowledgeCharacteristicCodes("color")
    Coating = MedicationKnowledgeCharacteristicCodes("coating")
    Scoring = MedicationKnowledgeCharacteristicCodes("scoring")
    Logo = MedicationKnowledgeCharacteristicCodes("logo")