from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class TimingAbbreviationCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-timing-abbreviation.html
    Code for a known / defined timing pattern.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "TimingAbbreviationCode"]) -> None:
            self.f: Callable[..., "TimingAbbreviationCode"] = f

        def __get__(
            self, obj: Any, owner: Type["TimingAbbreviationCode"]
        ) -> "TimingAbbreviationCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "TimingAbbreviationCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return TimingAbbreviationCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/timing-abbreviation
        """
        return "http://hl7.org/fhir/ValueSet/timing-abbreviation"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.78
        """
        return "2.16.840.1.113883.4.642.3.78"
