from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FHIRVersionCode(GenericTypeCode):
    """
    FHIRVersion
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
        All published FHIR Versions.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/FHIR-version
    """
    codeset: FhirUri = "http://hl7.org/fhir/FHIR-version"


class FHIRVersionCodeValues:
    """
    Oldest archived version of FHIR.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """

    _0_01 = FHIRVersionCode("0.01")
    """
    1st Draft for Comment (Sept 2012 Ballot).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_05 = FHIRVersionCode("0.05")
    """
    2nd Draft for Comment (January 2013 Ballot).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_06 = FHIRVersionCode("0.06")
    """
    DSTU 1 Ballot version.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_11 = FHIRVersionCode("0.11")
    """
    DSTU 1 Official version.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_0_80 = FHIRVersionCode("0.0.80")
    """
    DSTU 1 Official version Technical Errata #1.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_0_81 = FHIRVersionCode("0.0.81")
    """
    DSTU 1 Official version Technical Errata #2.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_0_82 = FHIRVersionCode("0.0.82")
    """
    Draft For Comment (January 2015 Ballot).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_4_0 = FHIRVersionCode("0.4.0")
    """
    DSTU 2 Ballot version (May 2015 Ballot).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _0_5_0 = FHIRVersionCode("0.5.0")
    """
    DSTU 2 QA Preview + CQIF Ballot (Sep 2015).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_0_0 = FHIRVersionCode("1.0.0")
    """
    DSTU 2 (Official version).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_0_1 = FHIRVersionCode("1.0.1")
    """
    DSTU 2 (Official version) with 1 technical errata.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_0_2 = FHIRVersionCode("1.0.2")
    """
    GAO Ballot + draft changes to main FHIR standard.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_1_0 = FHIRVersionCode("1.1.0")
    """
    CQF on FHIR Ballot + Connectathon 12 (Montreal).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_4_0 = FHIRVersionCode("1.4.0")
    """
    FHIR STU3 Ballot + Connectathon 13 (Baltimore).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_6_0 = FHIRVersionCode("1.6.0")
    """
    FHIR STU3 Candidate + Connectathon 14 (San Antonio).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _1_8_0 = FHIRVersionCode("1.8.0")
    """
    FHIR Release 3 (STU).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _3_0_0 = FHIRVersionCode("3.0.0")
    """
    FHIR Release 3 (STU) with 1 technical errata.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _3_0_1 = FHIRVersionCode("3.0.1")
    """
    R4 Ballot #1.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _3_3_0 = FHIRVersionCode("3.3.0")
    """
    R4 Ballot #2.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _3_5_0 = FHIRVersionCode("3.5.0")
    """
    FHIR Release 4 (Normative + STU).
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _4_0_0 = FHIRVersionCode("4.0.0")
    """
    FHIR Release 4 Technical Correction.
    From: http://hl7.org/fhir/FHIR-version in valuesets.xml
    """
    _4_0_1 = FHIRVersionCode("4.0.1")
