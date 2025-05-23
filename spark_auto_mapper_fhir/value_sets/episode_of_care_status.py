from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EpisodeOfCareStatusCode(GenericTypeCode):
    """
    EpisodeOfCareStatus
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
        The status of the episode of care.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/episode-of-care-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/episode-of-care-status"


class EpisodeOfCareStatusCodeValues:
    """
    This episode of care is planned to start at the date specified in the
    period.start. During this status, an organization may perform assessments to
    determine if the patient is eligible to receive services, or be organizing to
    make resources available to provide care services.
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """

    Planned = EpisodeOfCareStatusCode("planned")
    """
    This episode has been placed on a waitlist, pending the episode being made
    active (or cancelled).
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    Waitlist = EpisodeOfCareStatusCode("waitlist")
    """
    This episode of care is current.
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    Active = EpisodeOfCareStatusCode("active")
    """
    This episode of care is on hold; the organization has limited responsibility
    for the patient (such as while on respite).
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    OnHold = EpisodeOfCareStatusCode("onhold")
    """
    This episode of care is finished and the organization is not expecting to be
    providing further care to the patient. Can also be known as "closed",
    "completed" or other similar terms.
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    Finished = EpisodeOfCareStatusCode("finished")
    """
    The episode of care was cancelled, or withdrawn from service, often selected
    during the planned stage as the patient may have gone elsewhere, or the
    circumstances have changed and the organization is unable to provide the care.
    It indicates that services terminated outside the planned/expected workflow.
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    Cancelled = EpisodeOfCareStatusCode("cancelled")
    """
    This instance should not have been part of this patient's medical record.
    From: http://hl7.org/fhir/episode-of-care-status in valuesets.xml
    """
    EnteredInError = EpisodeOfCareStatusCode("entered-in-error")
