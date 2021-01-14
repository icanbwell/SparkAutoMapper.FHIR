from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ConditionCategoryCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-condition-category.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ConditionCategoryCode']) -> None:
            self.f: Callable[..., 'ConditionCategoryCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ConditionCategoryCode']
        ) -> 'ConditionCategoryCode':
            return self.f(owner)

    @classproperty
    def ProblemListItem(cls) -> 'ConditionCategoryCode':
        """
        An item on a problem list that can be managed over time and can be expressed by a practitioner
         (e.g. physician, nurse), patient, or related person.
        """
        # noinspection PyCallingNonCallable
        return ConditionCategoryCode("problem-list-item")

    @classproperty
    def EncounterDiagnosis(cls) -> 'ConditionCategoryCode':
        """
        A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter.
        """
        # noinspection PyCallingNonCallable
        return ConditionCategoryCode("encounter-diagnosis")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/condition-category
        """
        return "http://terminology.hl7.org/CodeSystem/condition-category"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.162
        """
        return "2.16.840.1.113883.4.642.3.162"
