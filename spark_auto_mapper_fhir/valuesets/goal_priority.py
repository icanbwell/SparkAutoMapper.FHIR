from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class GoalPriorityCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-goal-priority.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "GoalPriorityCode"]) -> None:
            self.f: Callable[..., "GoalPriorityCode"] = f

        def __get__(
            self, obj: Any, owner: Type["GoalPriorityCode"]
        ) -> "GoalPriorityCode":
            return self.f(owner)

    @classproperty
    def HighPriority(cls) -> "GoalPriorityCode":
        """
        Indicates that the goal is of considerable importance and should be a primary focus of care delivery.
        """
        # noinspection PyCallingNonCallable
        return GoalPriorityCode("high-priority")

    @classproperty
    def MediumPriority(cls) -> "GoalPriorityCode":
        """
        Indicates that the goal has a reasonable degree of importance and that concrete action should be taken
         towards the goal. Attainment is not as critical as high-priority goals.
        """
        # noinspection PyCallingNonCallable
        return GoalPriorityCode("medium-priority")

    @classproperty
    def LowPriority(cls) -> "GoalPriorityCode":
        """
        The goal is desirable but is not sufficiently important to devote significant resources to.
        Achievement of the goal may be sought when incidental to achieving other goals.
        """
        # noinspection PyCallingNonCallable
        return GoalPriorityCode("low-priority")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/goal-priority
        """
        return "http://terminology.hl7.org/CodeSystem/goal-priority"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.273
        """
        return "2.16.840.1.113883.4.642.3.273"
