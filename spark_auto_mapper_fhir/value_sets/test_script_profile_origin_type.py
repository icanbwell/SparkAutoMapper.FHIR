from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptProfileOriginTypeCode(GenericTypeCode):
    """
    TestScriptProfileOriginType
    From: http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types in valuesets.xml
        This value set defines a set of codes that are used to indicate the profile
    type of a test system when acting as the origin within a TestScript.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types"
    )


class TestScriptProfileOriginTypeCodeValues:
    """
    General FHIR client used to initiate operations against a FHIR server.
    From: http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types in valuesets.xml
    """

    FHIRClient = TestScriptProfileOriginTypeCode("FHIR-Client")
    """
    A FHIR client acting as a Structured Data Capture Form Filler.
    From: http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types in valuesets.xml
    """
    FHIRSDCFormFiller = TestScriptProfileOriginTypeCode("FHIR-SDC-FormFiller")
