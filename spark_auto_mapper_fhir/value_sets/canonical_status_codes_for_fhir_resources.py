from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CanonicalStatusCodesForFhirResources(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class CanonicalStatusCodesForFhirResourcesValues:
    Error = CanonicalStatusCodesForFhirResources("error")
    Proposed = CanonicalStatusCodesForFhirResources("proposed")
    Planned = CanonicalStatusCodesForFhirResources("planned")
    Draft = CanonicalStatusCodesForFhirResources("draft")
    Requested = CanonicalStatusCodesForFhirResources("requested")
    Received = CanonicalStatusCodesForFhirResources("received")
    Declined = CanonicalStatusCodesForFhirResources("declined")
    Accepted = CanonicalStatusCodesForFhirResources("accepted")
    Arrived = CanonicalStatusCodesForFhirResources("arrived")
    Active = CanonicalStatusCodesForFhirResources("active")
    Suspended = CanonicalStatusCodesForFhirResources("suspended")
    Failed = CanonicalStatusCodesForFhirResources("failed")
    Replaced = CanonicalStatusCodesForFhirResources("replaced")
    Complete = CanonicalStatusCodesForFhirResources("complete")
    Inactive = CanonicalStatusCodesForFhirResources("inactive")
    Abandoned = CanonicalStatusCodesForFhirResources("abandoned")
    Unknown = CanonicalStatusCodesForFhirResources("unknown")
    Unconfirmed = CanonicalStatusCodesForFhirResources("unconfirmed")
    Confirmed = CanonicalStatusCodesForFhirResources("confirmed")
    Resolved = CanonicalStatusCodesForFhirResources("resolved")
    Refuted = CanonicalStatusCodesForFhirResources("refuted")
    Differential = CanonicalStatusCodesForFhirResources("differential")
    Partial = CanonicalStatusCodesForFhirResources("partial")
    Busy_unavailable = CanonicalStatusCodesForFhirResources("busy-unavailable")
    Free = CanonicalStatusCodesForFhirResources("free")
    On_target = CanonicalStatusCodesForFhirResources("on-target")
    Ahead_of_target = CanonicalStatusCodesForFhirResources("ahead-of-target")
    Behind_target = CanonicalStatusCodesForFhirResources("behind-target")
    Not_ready = CanonicalStatusCodesForFhirResources("not-ready")
    Transduc_discon = CanonicalStatusCodesForFhirResources("transduc-discon")
    Hw_discon = CanonicalStatusCodesForFhirResources("hw-discon")