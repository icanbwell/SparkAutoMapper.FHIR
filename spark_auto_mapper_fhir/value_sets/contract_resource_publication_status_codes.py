from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractResourcePublicationStatusCodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ContractResourcePublicationStatusCodesValues:
    Amended = ContractResourcePublicationStatusCodes("amended")
    Appended = ContractResourcePublicationStatusCodes("appended")
    Cancelled = ContractResourcePublicationStatusCodes("cancelled")
    Disputed = ContractResourcePublicationStatusCodes("disputed")
    EnteredInError = ContractResourcePublicationStatusCodes("entered-in-error")
    Executable = ContractResourcePublicationStatusCodes("executable")
    Executed = ContractResourcePublicationStatusCodes("executed")
    Negotiable = ContractResourcePublicationStatusCodes("negotiable")
    Offered = ContractResourcePublicationStatusCodes("offered")
    Policy = ContractResourcePublicationStatusCodes("policy")
    Rejected = ContractResourcePublicationStatusCodes("rejected")
    Renewed = ContractResourcePublicationStatusCodes("renewed")
    Revoked = ContractResourcePublicationStatusCodes("revoked")
    Resolved = ContractResourcePublicationStatusCodes("resolved")
    Terminated = ContractResourcePublicationStatusCodes("terminated")