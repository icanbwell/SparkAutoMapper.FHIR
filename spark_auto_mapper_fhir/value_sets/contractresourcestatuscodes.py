from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Contractresourcestatuscodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ContractresourcestatuscodesValues:
    Amended = Contractresourcestatuscodes("amended")
    Appended = Contractresourcestatuscodes("appended")
    Cancelled = Contractresourcestatuscodes("cancelled")
    Disputed = Contractresourcestatuscodes("disputed")
    EnteredInError = Contractresourcestatuscodes("entered-in-error")
    Executable = Contractresourcestatuscodes("executable")
    Executed = Contractresourcestatuscodes("executed")
    Negotiable = Contractresourcestatuscodes("negotiable")
    Offered = Contractresourcestatuscodes("offered")
    Policy = Contractresourcestatuscodes("policy")
    Rejected = Contractresourcestatuscodes("rejected")
    Renewed = Contractresourcestatuscodes("renewed")
    Revoked = Contractresourcestatuscodes("revoked")
    Resolved = Contractresourcestatuscodes("resolved")
    Terminated = Contractresourcestatuscodes("terminated")