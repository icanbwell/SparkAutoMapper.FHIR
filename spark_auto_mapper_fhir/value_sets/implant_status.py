from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImplantStatusCode(GenericTypeCode):
    """
    Implant Status
    From: http://terminology.hl7.org/CodeSystem/implantStatus in valuesets.xml
        A set codes that define the functional status of an implanted device.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/implantStatus
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/implantStatus"


class ImplantStatusCodeValues:
    """
    The implanted device is working normally.
    From: http://terminology.hl7.org/CodeSystem/implantStatus in valuesets.xml
    """

    Functional = ImplantStatusCode("functional")
    """
    The implanted device is not working.
    From: http://terminology.hl7.org/CodeSystem/implantStatus in valuesets.xml
    """
    Non_Functional = ImplantStatusCode("non-functional")
    """
    The implanted device has been turned off.
    From: http://terminology.hl7.org/CodeSystem/implantStatus in valuesets.xml
    """
    Disabled = ImplantStatusCode("disabled")
    """
    the functional status of the implant has not been determined.
    From: http://terminology.hl7.org/CodeSystem/implantStatus in valuesets.xml
    """
    Unknown = ImplantStatusCode("unknown")
