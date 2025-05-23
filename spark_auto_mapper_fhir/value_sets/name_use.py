from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NameUseCode(GenericTypeCode):
    """
    NameUse
    From: http://hl7.org/fhir/name-use in valuesets.xml
        The use of a human name.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/name-use
    """
    codeset: FhirUri = "http://hl7.org/fhir/name-use"


class NameUseCodeValues:
    """
    Known as/conventional/the one you normally use.
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """

    Usual = NameUseCode("usual")
    """
    The formal name as registered in an official (government) registry, but which
    name might not be commonly used. May be called "legal name".
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """
    Official = NameUseCode("official")
    """
    A temporary name. Name.period can provide more detailed information. This may
    also be used for temporary names assigned at birth or in emergency situations.
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """
    Temp = NameUseCode("temp")
    """
    A name that is used to address the person in an informal manner, but is not
    part of their formal or usual name.
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """
    Nickname = NameUseCode("nickname")
    """
    Anonymous assigned name, alias, or pseudonym (used to protect a person's
    identity for privacy reasons).
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """
    Anonymous = NameUseCode("anonymous")
    """
    This name is no longer in use (or was never correct, but retained for
    records).
    From: http://hl7.org/fhir/name-use in valuesets.xml
    """
    Old = NameUseCode("old")
