from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageSelfPayCodesCode(GenericTypeCode):
    """
    CoverageSelfPayCodes
    From: http://terminology.hl7.org/CodeSystem/coverage-selfpay in valuesets.xml
        This value set includes Coverage SelfPay codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/coverage-selfpay
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/coverage-selfpay"


class CoverageSelfPayCodesCodeValues:
    """
    An individual or organization is paying directly for goods and services.
    From: http://terminology.hl7.org/CodeSystem/coverage-selfpay in valuesets.xml
    """

    Pay = CoverageSelfPayCodesCode("pay")
