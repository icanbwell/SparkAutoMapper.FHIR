from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EntityNameUseR2(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class EntityNameUseR2Values:
    Assumed = EntityNameUseR2("Assumed")
    Customary = EntityNameUseR2("C")
    MaidenName = EntityNameUseR2("M")
    Namerepresentationuse = EntityNameUseR2("NameRepresentationUse")
    NoLongerInUse = EntityNameUseR2("OLD")
    OfficialRegistryName = EntityNameUseR2("OR")
    Phonetic = EntityNameUseR2("PHON")
    Search = EntityNameUseR2("SRCH")
    Temporary = EntityNameUseR2("T")