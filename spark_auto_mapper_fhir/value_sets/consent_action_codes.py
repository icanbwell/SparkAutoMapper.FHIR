from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConsentActionCodesCode(GenericTypeCode):
    """
    ConsentActionCodes
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
        This value set includes sample Consent Action codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/consentaction
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/consentaction"


class ConsentActionCodesCodeValues:
    """
    Gather retrieved information for storage
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
    """

    Collect = ConsentActionCodesCode("collect")
    """
    Retrieval without permitting collection, use or disclosure. e.g., no screen-
    scraping for collection, use or disclosure (view-only access)
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
    """
    Access = ConsentActionCodesCode("access")
    """
    Utilize the retrieved information
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
    """
    Use = ConsentActionCodesCode("use")
    """
    Transfer retrieved information
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
    """
    Disclose = ConsentActionCodesCode("disclose")
    """
    Allow retrieval of a patient's information for the purpose of update or
    rectify
    From: http://terminology.hl7.org/CodeSystem/consentaction in valuesets.xml
    """
    AccessAndCorrect = ConsentActionCodesCode("correct")
