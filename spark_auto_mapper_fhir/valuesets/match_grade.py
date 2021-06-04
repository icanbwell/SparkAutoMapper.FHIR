from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MatchGradeCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR properties not just the ones you need
    https://www.hl7.org/fhir/valueset-match-grade.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MatchGradeCode"]) -> None:
            self.f: Callable[..., "MatchGradeCode"] = f

        def __get__(self, obj: Any, owner: Type["MatchGradeCode"]) -> "MatchGradeCode":
            return self.f(owner)

    @classproperty
    def CertainMatch(cls) -> "MatchGradeCode":
        """
        This record meets the matching criteria to be automatically considered as a full match.
        """
        # noinspection PyCallingNonCallable
        return MatchGradeCode("certain")

    @classproperty
    def ProbableMatch(cls) -> "MatchGradeCode":
        """
        This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required before using this as a match.
        """
        # noinspection PyCallingNonCallable
        return MatchGradeCode("probable")

    @classproperty
    def PossibleMatch(cls) -> "MatchGradeCode":
        """
        This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as a match.
        """
        # noinspection PyCallingNonCallable
        return MatchGradeCode("possible")

    @classproperty
    def CertainlyNotAMatch(cls) -> "MatchGradeCode":
        """
        This record is known not to be a match. Note that usually non-matching records are not returned, but in some cases records previously or likely considered as a match may specifically be negated by the matching engine.
        """
        # noinspection PyCallingNonCallable
        return MatchGradeCode("certainly-not")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/match-grade
        """
        return "http://terminology.hl7.org/CodeSystem/match-grade"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.970
        """
        return "2.16.840.1.113883.4.642.3.970"
