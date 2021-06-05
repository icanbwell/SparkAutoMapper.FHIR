from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionGroupingBehaviorCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-grouping-behavior.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionGroupingBehaviorCode"]) -> None:
            self.f: Callable[..., "ActionGroupingBehaviorCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionGroupingBehaviorCode"]
        ) -> "ActionGroupingBehaviorCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ActionGroupingBehaviorCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ActionGroupingBehaviorCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-grouping-behavior
        """
        return "http://hl7.org/fhir/ValueSet/action-grouping-behavior"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.799
        """
        return "2.16.840.1.113883.4.642.3.799"
