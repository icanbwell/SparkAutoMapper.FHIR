from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractResourceLegalStateCodesCode(GenericTypeCode):
    """
    ContractResourceLegalStateCodes
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
        This value set contract specific codes for status.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/contract-legalstate
    """
    codeset: FhirUri = "http://hl7.org/fhir/contract-legalstate"


class ContractResourceLegalStateCodesCodeValues:
    """
    Contract is augmented with additional information to correct errors in a
    predecessor or to updated values in a predecessor. Usage: Contract altered
    within effective time. Precedence Order = 9. Comparable FHIR and v.3 status
    codes: revised; replaced.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """

    Amended = ContractResourceLegalStateCodesCode("amended")
    """
    Contract is augmented with additional information that was missing from a
    predecessor Contract. Usage: Contract altered within effective time.
    Precedence Order = 9. Comparable FHIR and v.3 status codes: updated, replaced.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Appended = ContractResourceLegalStateCodesCode("appended")
    """
    Contract is terminated due to failure of the Grantor and/or the Grantee to
    fulfil one or more contract provisions. Usage: Abnormal contract termination.
    Precedence Order = 10. Comparable FHIR and v.3 status codes: stopped; failed;
    aborted.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Cancelled = ContractResourceLegalStateCodesCode("cancelled")
    """
    Contract is pended to rectify failure of the Grantor or the Grantee to fulfil
    contract provision(s). E.g., Grantee complaint about Grantor's failure to
    comply with contract provisions. Usage: Contract pended. Precedence Order = 7.
    Comparable FHIR and v.3 status codes: on hold; pended; suspended.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Disputed = ContractResourceLegalStateCodesCode("disputed")
    """
    Contract was created in error. No Precedence Order.  Status may be applied to
    a Contract with any status.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    EnteredInError = ContractResourceLegalStateCodesCode("entered-in-error")
    """
    Contract execution pending; may be executed when either the Grantor or the
    Grantee accepts the contract provisions by signing. I.e., where either the
    Grantor or the Grantee has signed, but not both. E.g., when an insurance
    applicant signs the insurers application, which references the policy. Usage:
    Optional first step of contract execution activity.  May be skipped and
    contracting activity moves directly to executed state. Precedence Order = 3.
    Comparable FHIR and v.3 status codes: draft; preliminary; planned; intended;
    active.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Executable = ContractResourceLegalStateCodesCode("executable")
    """
    Contract is activated for period stipulated when both the Grantor and Grantee
    have signed it. Usage: Required state for normal completion of contracting
    activity.  Precedence Order = 6. Comparable FHIR and v.3 status codes:
    accepted; completed.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Executed = ContractResourceLegalStateCodesCode("executed")
    """
    Contract execution is suspended while either or both the Grantor and Grantee
    propose and consider new or revised contract provisions. I.e., where the party
    which has not signed proposes changes to the terms.  E .g., a life insurer
    declines to agree to the signed application because the life insurer has
    evidence that the applicant, who asserted to being younger or a non-smoker to
    get a lower premium rate - but offers instead to agree to a higher premium
    based on the applicants actual age or smoking status. Usage: Optional contract
    activity between executable and executed state. Precedence Order = 4.
    Comparable FHIR and v.3 status codes: in progress; review; held.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Negotiable = ContractResourceLegalStateCodesCode("negotiable")
    """
    Contract is a proposal by either the Grantor or the Grantee. Aka - A Contract
    hard copy or electronic 'template', 'form' or 'application'. E.g., health
    insurance application; consent directive form. Usage: Beginning of contract
    negotiation, which may have been completed as a precondition because used for
    0..* contracts. Precedence Order = 2. Comparable FHIR and v.3 status codes:
    requested; new.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Offered = ContractResourceLegalStateCodesCode("offered")
    """
    Contract template is available as the basis for an application or offer by the
    Grantor or Grantee. E.g., health insurance policy; consent directive policy.
    Usage: Required initial contract activity, which may have been completed as a
    precondition because used for 0..* contracts. Precedence Order = 1. Comparable
    FHIR and v.3 status codes: proposed; intended.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Policy = ContractResourceLegalStateCodesCode("policy")
    """
     Execution of the Contract is not completed because either or both the Grantor
    and Grantee decline to accept some or all of the contract provisions. Usage:
    Optional contract activity between executable and abnormal termination.
    Precedence Order = 5. Comparable FHIR and v.3 status codes:  stopped;
    cancelled.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Rejected = ContractResourceLegalStateCodesCode("rejected")
    """
    Beginning of a successor Contract at the termination of predecessor Contract
    lifecycle. Usage: Follows termination of a preceding Contract that has reached
    its expiry date. Precedence Order = 13. Comparable FHIR and v.3 status codes:
    superseded.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Renewed = ContractResourceLegalStateCodesCode("renewed")
    """
    A Contract that is rescinded.  May be required prior to replacing with an
    updated Contract. Comparable FHIR and v.3 status codes: nullified.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Revoked = ContractResourceLegalStateCodesCode("revoked")
    """
    Contract is reactivated after being pended because of faulty execution. *E.g.,
    competency of the signer(s), or where the policy is substantially different
    from and did not accompany the application/form so that the applicant could
    not compare them. Aka - ''reactivated''. Usage: Optional stage where a pended
    contract is reactivated. Precedence Order = 8. Comparable FHIR and v.3 status
    codes: reactivated.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Resolved = ContractResourceLegalStateCodesCode("resolved")
    """
    Contract reaches its expiry date. It might or might not be renewed or
    renegotiated. Usage: Normal end of contract period. Precedence Order = 12.
    Comparable FHIR and v.3 status codes: Obsoleted.
    From: http://hl7.org/fhir/contract-legalstate in valuesets.xml
    """
    Terminated = ContractResourceLegalStateCodesCode("terminated")
