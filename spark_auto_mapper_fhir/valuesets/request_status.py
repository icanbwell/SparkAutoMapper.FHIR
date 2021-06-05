from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RequestStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-request-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "RequestStatusCode"]) -> None:
            self.f: Callable[..., "RequestStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["RequestStatusCode"]
        ) -> "RequestStatusCode":
            return self.f(owner)

    @classproperty
    def Draft(cls) -> "RequestStatusCode":
        """
        The request has been created but is not yet complete or ready for action.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("draft")

    @classproperty
    def Active(cls) -> "RequestStatusCode":
        """
        The request is in force and ready to be acted upon.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("active")

    @classproperty
    def OnHold(cls) -> "RequestStatusCode":
        """
        The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in the future.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("on-hold")

    @classproperty
    def Revoked(cls) -> "RequestStatusCode":
        """
        The request (and any implicit authorization to act) has been terminated prior to the known full completion of the intended actions. No further activity should occur.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("revoked")

    @classproperty
    def Completed(cls) -> "RequestStatusCode":
        """
        The activity described by the request has been fully performed. No further activity will occur.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("completed")

    @classproperty
    def EnteredInError(cls) -> "RequestStatusCode":
        """
        This request should never have existed and should be considered 'void'. (It is possible that real-world decisions were based on it. If real-world activity has occurred, the status should be "revoked" rather than "entered-in-error".).
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("entered-in-error")

    @classproperty
    def Unknown(cls) -> "RequestStatusCode":
        """
        The authoring/source system does not know which of the status values currently applies for this request. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.
        """
        # noinspection PyCallingNonCallable
        return RequestStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/request-status
        """
        return "http://hl7.org/fhir/ValueSet/request-status"
