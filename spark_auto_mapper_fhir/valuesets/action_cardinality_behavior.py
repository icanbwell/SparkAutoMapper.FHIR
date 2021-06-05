from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionCardinalityBehaviorCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-cardinality-behavior.html
    Defines behavior for an action or a group for how many times that item may be repeated.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionCardinalityBehaviorCode"]) -> None:
            self.f: Callable[..., "ActionCardinalityBehaviorCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionCardinalityBehaviorCode"]
        ) -> "ActionCardinalityBehaviorCode":
            return self.f(owner)

    @classproperty
    def Single(cls) -> "ActionCardinalityBehaviorCode":
        """
        The action may only be selected one time.
        """
        # noinspection PyCallingNonCallable
        return ActionCardinalityBehaviorCode("single")

    @classproperty
    def Multiple(cls) -> "ActionCardinalityBehaviorCode":
        """
        The action may be selected multiple times.
        """
        # noinspection PyCallingNonCallable
        return ActionCardinalityBehaviorCode("multiple")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-cardinality-behavior
        """
        return "http://hl7.org/fhir/ValueSet/action-cardinality-behavior"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.807
        """
        return "2.16.840.1.113883.4.642.3.807"
