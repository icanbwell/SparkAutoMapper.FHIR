from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NhinPurposeofuse(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class NhinPurposeofuseValues:
    Treatment = NhinPurposeofuse("TREATMENT")
    Payment = NhinPurposeofuse("PAYMENT")
    Operations = NhinPurposeofuse("OPERATIONS")
    Sysadmin = NhinPurposeofuse("SYSADMIN")
    Fraud = NhinPurposeofuse("FRAUD")
    Psychotherapy = NhinPurposeofuse("PSYCHOTHERAPY")
    Training = NhinPurposeofuse("TRAINING")
    Legal = NhinPurposeofuse("LEGAL")
    Marketing = NhinPurposeofuse("MARKETING")
    Directory = NhinPurposeofuse("DIRECTORY")
    Family = NhinPurposeofuse("FAMILY")
    Present = NhinPurposeofuse("PRESENT")
    Emergency = NhinPurposeofuse("EMERGENCY")
    Disaster = NhinPurposeofuse("DISASTER")
    PublicHealth = NhinPurposeofuse("PUBLICHEALTH")
    Abuse = NhinPurposeofuse("ABUSE")
    Oversight = NhinPurposeofuse("OVERSIGHT")
    Judicial = NhinPurposeofuse("JUDICIAL")
    LawEnforcement = NhinPurposeofuse("LAW")
    Deceased = NhinPurposeofuse("DECEASED")
    Donation = NhinPurposeofuse("DONATION")
    Research = NhinPurposeofuse("RESEARCH")
    Threat = NhinPurposeofuse("THREAT")
    Government = NhinPurposeofuse("GOVERNMENT")
    Worker_sComp = NhinPurposeofuse("WORKERSCOMP")
    Coverage = NhinPurposeofuse("COVERAGE")
    Request = NhinPurposeofuse("REQUEST")