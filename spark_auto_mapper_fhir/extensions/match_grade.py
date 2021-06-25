from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.custom.match_grade_extension_item import (
    MatchGradeExtensionItem,
)
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.value_sets.match_grade import MatchGradeCode


class MatchGrade(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, match_grade: MatchGradeCode) -> None:
        """
        MatchGrade Extension type in FHIR

        :param match_grade: Assessment of resource match outcome - how likely this resource is to be a match.
        """
        extensions = [
            MatchGradeExtensionItem(
                url="http://hl7.org/fhir/StructureDefinition/match-grade",
                valueString=match_grade,
            )
        ]
        super().__init__(url=self.__class__.codeset, extension=FhirList(extensions))

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/StructureDefinition/match-grade"
