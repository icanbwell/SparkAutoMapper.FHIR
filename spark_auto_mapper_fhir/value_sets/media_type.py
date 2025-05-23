from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MediaTypeCode(GenericTypeCode):
    """
    MediaType
    From: http://terminology.hl7.org/CodeSystem/media-type in valuesets.xml
        Codes for high level media categories.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/media-type
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/media-type"


class MediaTypeCodeValues:
    """
    The media consists of one or more unmoving images, including photographs,
    computer-generated graphs and charts, and scanned documents
    From: http://terminology.hl7.org/CodeSystem/media-type in valuesets.xml
    """

    Image = MediaTypeCode("image")
    """
    The media consists of a series of frames that capture a moving image
    From: http://terminology.hl7.org/CodeSystem/media-type in valuesets.xml
    """
    Video = MediaTypeCode("video")
    """
    The media consists of a sound recording
    From: http://terminology.hl7.org/CodeSystem/media-type in valuesets.xml
    """
    Audio = MediaTypeCode("audio")
