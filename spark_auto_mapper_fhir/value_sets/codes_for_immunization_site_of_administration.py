from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CodesForImmunizationSiteOfAdministrationCode(GenericTypeCode):
    """
    CodesForImmunizationSiteOfAdministration
    From: http://hl7.org/fhir/ValueSet/immunization-site in valuesets.xml
        The value set to instantiate this attribute should be drawn from a
    terminologically robust code system that consists of or contains concepts to
    support describing the body site where the vaccination occurred. This value
    set is provided as a suggestive example.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ActSite
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ActSite"


class CodesForImmunizationSiteOfAdministrationCodeValues:
    """
    An anatomical location on a human which can be the focus of an act.
    From: http://terminology.hl7.org/CodeSystem/v3-ActSite in v3-codesystems.xml
    """

    HumanActSite = CodesForImmunizationSiteOfAdministrationCode("_HumanActSite")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-site in valuesets.xml
    """
    LeftArm = CodesForImmunizationSiteOfAdministrationCode("LA")
    """
    From: http://hl7.org/fhir/ValueSet/immunization-site in valuesets.xml
    """
    RightArm = CodesForImmunizationSiteOfAdministrationCode("RA")
