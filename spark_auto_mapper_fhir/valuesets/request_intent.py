from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class RequestIntentCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-request-intent.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "RequestIntentCode"]) -> None:
            self.f: Callable[..., "RequestIntentCode"] = f

        def __get__(
            self, obj: Any, owner: Type["RequestIntentCode"]
        ) -> "RequestIntentCode":
            return self.f(owner)

    @classproperty
    def Proposal(cls) -> "RequestIntentCode":
        """
        The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and without providing an authorization to act.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("proposal")

    @classproperty
    def Plan(cls) -> "RequestIntentCode":
        """
        The request represents an intention to ensure something occurs without providing an authorization for others to act.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("plan")

    @classproperty
    def Directive(cls) -> "RequestIntentCode":
        """
        The request represents a legally binding instruction authored by a Patient or RelatedPerson.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("directive")

    @classproperty
    def Order(cls) -> "RequestIntentCode":
        """
        The request represents a request/demand and authorization for action by a Practitioner.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("order")

    @classproperty
    def OriginalOrder(cls) -> "RequestIntentCode":
        """
        The request represents an original authorization for action.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("original-order")

    @classproperty
    def ReflexOrder(cls) -> "RequestIntentCode":
        """
        The request represents an automatically generated supplemental authorization for action based on a parent authorization together with initial results of the action taken against that parent authorization.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("reflex-order")

    @classproperty
    def FillerOrder(cls) -> "RequestIntentCode":
        """
        The request represents the view of an authorization instantiated by a fulfilling system representing the details of the fulfiller's intention to act upon a submitted order.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("filler-order")

    @classproperty
    def InstanceOrder(cls) -> "RequestIntentCode":
        """
        An order created in fulfillment of a broader order that represents the authorization for a single activity occurrence. E.g. The administration of a single dose of a drug.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("instance-order")

    @classproperty
    def Option(cls) -> "RequestIntentCode":
        """
        The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or other constraints among a set of requests. Refer to [[[RequestGroup]]] for additional information on how this status is used.
        """
        # noinspection PyCallingNonCallable
        return RequestIntentCode("option")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"
