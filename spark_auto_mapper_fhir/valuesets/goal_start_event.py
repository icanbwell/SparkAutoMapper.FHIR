from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class GoalStartEventCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-goal-start-event.html
    Identifies types of events that might trigger the start of a goal.
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'GoalStartEventCode']) -> None:
            self.f: Callable[..., 'GoalStartEventCode'] = f

        def __get__(
            self, obj: Any, owner: Type['GoalStartEventCode']
        ) -> 'GoalStartEventCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'GoalStartEventCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return GoalStartEventCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.279
        """
        return "2.16.840.1.113883.4.642.3.279"
