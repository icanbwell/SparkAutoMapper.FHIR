from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionConditionKindCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-condition-kind.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionConditionKindCode"]) -> None:
            self.f: Callable[..., "ActionConditionKindCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionConditionKindCode"]
        ) -> "ActionConditionKindCode":
            return self.f(owner)

    @classproperty
    def applicability(cls) -> "ActionConditionKindCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ActionConditionKindCode("applicability")

    @classproperty
    def start(cls) -> "ActionConditionKindCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ActionConditionKindCode("start")

    @classproperty
    def stop(cls) -> "ActionConditionKindCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ActionConditionKindCode("stop")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-condition-kind
        """
        return "http://hl7.org/fhir/ValueSet/action-condition-kind"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.815
        """
        return "2.16.840.1.113883.4.642.3.815"
