from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MeasureImprovementNotationCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-measure-improvement-notation.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MeasureImprovementNotationCode"]) -> None:
            self.f: Callable[..., "MeasureImprovementNotationCode"] = f

        def __get__(
            self, obj: Any, owner: Type["MeasureImprovementNotationCode"]
        ) -> "MeasureImprovementNotationCode":
            return self.f(owner)

    @classproperty
    def Increase(cls) -> "MeasureImprovementNotationCode":
        """
        Improvement is indicated as an increase in the score or measurement (e.g. Higher score indicates better quality).
        """
        # noinspection PyCallingNonCallable
        return MeasureImprovementNotationCode("increase")

    @classproperty
    def Decrease(cls) -> "MeasureImprovementNotationCode":
        """
        Improvement is indicated as a decrease in the score or measurement (e.g. Lower score indicates better quality).
        """
        # noinspection PyCallingNonCallable
        return MeasureImprovementNotationCode("decrease")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/measure-improvement-notation"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.1236"
