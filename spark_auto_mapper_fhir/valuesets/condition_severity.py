from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ConditionSeverityCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-condition-severity.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ConditionSeverityCode']) -> None:
            self.f: Callable[..., 'ConditionSeverityCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ConditionSeverityCode']
        ) -> 'ConditionSeverityCode':
            return self.f(owner)

    @classproperty
    def Severe(cls) -> 'ConditionSeverityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ConditionSeverityCode("24484000")

    @classproperty
    def Moderate(cls) -> 'ConditionSeverityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ConditionSeverityCode("6736007")

    @classproperty
    def Mild(cls) -> 'ConditionSeverityCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ConditionSeverityCode("255604002")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://snomed.info/sct
        """
        return "http://snomed.info/sct"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.168
        """
        return "2.16.840.1.113883.4.642.3.168"
