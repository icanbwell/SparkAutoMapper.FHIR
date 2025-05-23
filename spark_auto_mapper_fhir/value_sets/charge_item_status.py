from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ChargeItemStatusCode(GenericTypeCode):
    """
    ChargeItemStatus
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
        Codes identifying the lifecycle stage of a ChargeItem.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/chargeitem-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/chargeitem-status"


class ChargeItemStatusCodeValues:
    """
    The charge item has been entered, but the charged service is not  yet
    complete, so it shall not be billed yet but might be used in the context of
    pre-authorization.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """

    Planned = ChargeItemStatusCode("planned")
    """
    The charge item is ready for billing.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    Billable = ChargeItemStatusCode("billable")
    """
    The charge item has been determined to be not billable (e.g. due to rules
    associated with the billing code).
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    NotBillable = ChargeItemStatusCode("not-billable")
    """
    The processing of the charge was aborted.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    Aborted = ChargeItemStatusCode("aborted")
    """
    The charge item has been billed (e.g. a billing engine has generated financial
    transactions by applying the associated ruled for the charge item to the
    context of the Encounter, and placed them into Claims/Invoices.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    Billed = ChargeItemStatusCode("billed")
    """
    The charge item has been entered in error and should not be processed for
    billing.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    EnteredInError = ChargeItemStatusCode("entered-in-error")
    """
    The authoring system does not know which of the status values currently
    applies for this charge item  Note: This concept is not to be used for "other"
    - one of the listed statuses is presumed to apply, it's just not known which
    one.
    From: http://hl7.org/fhir/chargeitem-status in valuesets.xml
    """
    Unknown = ChargeItemStatusCode("unknown")
