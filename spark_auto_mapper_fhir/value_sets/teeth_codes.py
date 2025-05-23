from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TeethCodesCode(GenericTypeCode):
    """
    TeethCodes
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
        This value set includes the FDI Teeth codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ex-fdi
    """
    codeset: FhirUri = "http://hl7.org/fhir/ex-fdi"


class TeethCodesCodeValues:
    """
    Upper Right Tooth 1 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """

    _11 = TeethCodesCode("11")
    """
    Upper Right Tooth 2 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _12 = TeethCodesCode("12")
    """
    Upper Right Tooth 3 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _13 = TeethCodesCode("13")
    """
    Upper Right Tooth 4 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _14 = TeethCodesCode("14")
    """
    Upper Right Tooth 5 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _15 = TeethCodesCode("15")
    """
    Upper Right Tooth 6 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _16 = TeethCodesCode("16")
    """
    Upper Right Tooth 7 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _17 = TeethCodesCode("17")
    """
    Upper Right Tooth 8 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _18 = TeethCodesCode("18")
    """
    Upper Left Tooth 1 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _21 = TeethCodesCode("21")
    """
    Upper Left Tooth 2 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _22 = TeethCodesCode("22")
    """
    Upper Left Tooth 3 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _23 = TeethCodesCode("23")
    """
    Upper Left Tooth 4 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _24 = TeethCodesCode("24")
    """
    Upper Left Tooth 5 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _25 = TeethCodesCode("25")
    """
    Upper Left Tooth 6 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _26 = TeethCodesCode("26")
    """
    Upper Left Tooth 7 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _27 = TeethCodesCode("27")
    """
    Upper Left Tooth 8 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _28 = TeethCodesCode("28")
    """
    Lower Left Tooth 1 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _31 = TeethCodesCode("31")
    """
    Lower Left Tooth 2 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _32 = TeethCodesCode("32")
    """
    Lower Left Tooth 3 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _33 = TeethCodesCode("33")
    """
    Lower Left Tooth 4 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _34 = TeethCodesCode("34")
    """
    Lower Left Tooth 5 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _35 = TeethCodesCode("35")
    """
    Lower Left Tooth 6 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _36 = TeethCodesCode("36")
    """
    Lower Left Tooth 7 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _37 = TeethCodesCode("37")
    """
    Lower Left Tooth 8 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _38 = TeethCodesCode("38")
    """
    Lower Right Tooth 1 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _41 = TeethCodesCode("41")
    """
    Lower Right Tooth 2 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _42 = TeethCodesCode("42")
    """
    Lower Right Tooth 3 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _43 = TeethCodesCode("43")
    """
    Lower Right Tooth 4 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _44 = TeethCodesCode("44")
    """
    Lower Right Tooth 5 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _45 = TeethCodesCode("45")
    """
    Lower Right Tooth 6 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _46 = TeethCodesCode("46")
    """
    Lower Right Tooth 7 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _47 = TeethCodesCode("47")
    """
    Lower Right Tooth 8 from the central axis, permanent dentition.
    From: http://hl7.org/fhir/ex-fdi in valuesets.xml
    """
    _48 = TeethCodesCode("48")
