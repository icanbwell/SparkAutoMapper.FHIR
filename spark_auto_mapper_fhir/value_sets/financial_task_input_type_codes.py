from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FinancialTaskInputTypeCodesCode(GenericTypeCode):
    """
    FinancialTaskInputTypeCodes
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
        This value set includes Financial Task Input Type codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/financialtaskinputtype
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/financialtaskinputtype"


class FinancialTaskInputTypeCodesCodeValues:
    """
    The name of a resource to include in a selection.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """

    Include = FinancialTaskInputTypeCodesCode("include")
    """
    The name of a resource to not include in a selection.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    Exclude = FinancialTaskInputTypeCodesCode("exclude")
    """
    A reference to the response resource to the original processing of a resource.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    OriginalResponse = FinancialTaskInputTypeCodesCode("origresponse")
    """
    A reference value which must be quoted to authorize an action.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    ReferenceNumber = FinancialTaskInputTypeCodesCode("reference")
    """
    The sequence number associated with an item for reprocessing.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    ItemNumber = FinancialTaskInputTypeCodesCode("item")
    """
    The reference period for the action being requested.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    Period = FinancialTaskInputTypeCodesCode("period")
    """
    The processing status from a check on the processing status of a resource such
    as the adjudication of a claim.
    From: http://terminology.hl7.org/CodeSystem/financialtaskinputtype in valuesets.xml
    """
    StatusCode = FinancialTaskInputTypeCodesCode("status")
