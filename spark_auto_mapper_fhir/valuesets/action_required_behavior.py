from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionRequiredBehaviorCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-required-behavior.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ActionRequiredBehaviorCode']
        ) -> None:
            self.f: Callable[..., 'ActionRequiredBehaviorCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ActionRequiredBehaviorCode']
        ) -> 'ActionRequiredBehaviorCode':
            return self.f(owner)

    @classproperty
    def Must(cls) -> 'ActionRequiredBehaviorCode':
        """
        An action with this behavior must be included in the actions processed by the end user; the end user SHALL NOT choose not to include this action.
        """
        # noinspection PyCallingNonCallable
        return ActionRequiredBehaviorCode("must")

    @classproperty
    def Could(cls) -> 'ActionRequiredBehaviorCode':
        """
        An action with this behavior may be included in the set of actions processed by the end user.
        """
        # noinspection PyCallingNonCallable
        return ActionRequiredBehaviorCode("could")

    @classproperty
    def MustUnlessDocumented(cls) -> 'ActionRequiredBehaviorCode':
        """
        An action with this behavior must be included in the set of actions processed by the end user,
        unless the end user provides documentation as to why the action was not included.
        """
        # noinspection PyCallingNonCallable
        return ActionRequiredBehaviorCode("must-unless-documented")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-required-behavior
        """
        return "http://hl7.org/fhir/ValueSet/action-required-behavior"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.803
        """
        return "2.16.840.1.113883.4.642.3.803"
