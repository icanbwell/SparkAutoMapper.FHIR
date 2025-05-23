from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SequenceTypeCode(GenericTypeCode):
    """
    sequenceType
    From: http://hl7.org/fhir/sequence-type in valuesets.xml
        Type if a sequence -- DNA, RNA, or amino acid sequence.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/sequence-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/sequence-type"


class SequenceTypeCodeValues:
    """
    Amino acid sequence.
    From: http://hl7.org/fhir/sequence-type in valuesets.xml
    """

    AASequence = SequenceTypeCode("aa")
    """
    DNA Sequence.
    From: http://hl7.org/fhir/sequence-type in valuesets.xml
    """
    DNASequence = SequenceTypeCode("dna")
    """
    RNA Sequence.
    From: http://hl7.org/fhir/sequence-type in valuesets.xml
    """
    RNASequence = SequenceTypeCode("rna")
