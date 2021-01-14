from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ObservationStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-observation-status.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ObservationStatusCode']) -> None:
            self.f: Callable[..., 'ObservationStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ObservationStatusCode']
        ) -> 'ObservationStatusCode':
            return self.f(owner)

    @classproperty
    def Registered(cls) -> 'ObservationStatusCode':
        """
        The existence of the observation is registered, but there is no result yet available.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("registered")

    @classproperty
    def Preliminary(cls) -> 'ObservationStatusCode':
        """
        This is an initial or interim observation: data may be incomplete or unverified.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("preliminary")

    @classproperty
    def Final(cls) -> 'ObservationStatusCode':
        """
        The observation is complete and there are no further actions needed. Additional information such "released"
        , "signed", etc would be represented using [Provenance](provenance.html) which provides not only the act
         but also the actors and dates and other related data. These act states would be associated with an
         observation status of `preliminary` until they are all completed and then a status of `final` would be applied.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("final")

    @classproperty
    def Amended(cls) -> 'ObservationStatusCode':
        """
        Subsequent to being Final, the observation has been modified subsequent. This includes
        updates/new information and corrections.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("amended")

    @classproperty
    def Corrected(cls) -> 'ObservationStatusCode':
        """
        Subsequent to being Final, the observation has been modified to correct an error in the test result.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("corrected")

    @classproperty
    def Cancelled(cls) -> 'ObservationStatusCode':
        """
        The observation is unavailable because the measurement was not started or not completed
        (also sometimes called "aborted").
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("cancelled")

    @classproperty
    def EnteredInError(cls) -> 'ObservationStatusCode':
        """
        The observation has been withdrawn following previous final release. This electronic record should never
         have existed, though it is possible that real-world decisions were based on it. (If real-world activity
          has occurred, the status should be "cancelled" rather than "entered-in-error".).
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("entered-in-error")

    @classproperty
    def Unknown(cls) -> 'ObservationStatusCode':
        """
        The authoring/source system does not know which of the status values currently applies for this observation.
        Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply,
        but the authoring/source system does not know which.
        """
        # noinspection PyCallingNonCallable
        return ObservationStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/observation-status
        """
        return "http://hl7.org/fhir/observation-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.400
        """
        return "2.16.840.1.113883.4.642.3.400"
