from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming,SpellCheckingInspection
class ActionPrecheckBehaviorCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-precheck-behavior.html
    Defines selection frequency behavior for an action or group.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionPrecheckBehaviorCode"]) -> None:
            self.f: Callable[..., "ActionPrecheckBehaviorCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionPrecheckBehaviorCode"]
        ) -> "ActionPrecheckBehaviorCode":
            return self.f(owner)

    @classproperty
    def Yes(cls) -> "ActionPrecheckBehaviorCode":
        """
        An action with this behavior is one of the most frequent action that is, or should be, included by an end user,
         for the particular context in which the action occurs. The system displaying the action to the end user should
          consider "pre-checking" such an action as a convenience for the user.
        """
        # noinspection PyCallingNonCallable
        return ActionPrecheckBehaviorCode("yes")

    @classproperty
    def No(cls) -> "ActionPrecheckBehaviorCode":
        """
        An action with this behavior is one of the less frequent actions included by the end user, for the
        particular context in which the action occurs. The system displaying the actions to the end user
        would typically not "pre-check" such an action.
        """
        # noinspection PyCallingNonCallable
        return ActionPrecheckBehaviorCode("no")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-precheck-behavior
        """
        return "http://hl7.org/fhir/ValueSet/action-precheck-behavior"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.805
        """
        return "2.16.840.1.113883.4.642.3.805"
