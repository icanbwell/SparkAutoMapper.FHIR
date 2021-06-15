from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EpisodeOfCareStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-episode-of-care-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EpisodeOfCareStatusCode"]) -> None:
            self.f: Callable[..., "EpisodeOfCareStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EpisodeOfCareStatusCode"]
        ) -> "EpisodeOfCareStatusCode":
            return self.f(owner)

    @classproperty
    def Planned(cls) -> "EpisodeOfCareStatusCode":
        """
        This episode of care is planned to start at the date specified in the period.start.
        During this status, an organization may perform assessments to determine if the patient is eligible to receive services,
        or be organizing to make resources available to provide care services.
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("planned")

    @classproperty
    def Waitlist(cls) -> "EpisodeOfCareStatusCode":
        """
        This episode has been placed on a waitlist, pending the episode being made active (or cancelled).
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("waitlist")

    @classproperty
    def Active(cls) -> "EpisodeOfCareStatusCode":
        """
        This episode of care is current.
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("active")

    @classproperty
    def OnHold(cls) -> "EpisodeOfCareStatusCode":
        """
        This episode of care is on hold;
        the organization has limited responsibility for the patient (such as while on respite).
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("onhold")

    @classproperty
    def Finished(cls) -> "EpisodeOfCareStatusCode":
        """
        This episode of care is finished and the organization is not expecting
        to be providing further care to the patient.
        Can also be known as "closed", "completed" or other similar terms.
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("finished")

    @classproperty
    def Cancelled(cls) -> "EpisodeOfCareStatusCode":
        """
        The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the care.
        It indicates that services terminated outside the planned/expected workflow.
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("cancelled")

    @classproperty
    def EnteredInError(cls) -> "EpisodeOfCareStatusCode":
        """
        This instance should not have been part of this patient's medical record.
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareStatusCode("entered-in-error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/episode-of-care-status
        """
        return "http://hl7.org/fhir/ValueSet/episode-of-care-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.664
        """
        return "2.16.840.1.113883.4.642.3.664"
