from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EpisodeOfCareTypeCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-episodeofcare-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EpisodeOfCareTypeCode"]) -> None:
            self.f: Callable[..., "EpisodeOfCareTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EpisodeOfCareTypeCode"]
        ) -> "EpisodeOfCareTypeCode":
            return self.f(owner)

    @classproperty
    def HomeAndCommunityCare(cls) -> "EpisodeOfCareTypeCode":
        """
        Home and Community Care
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareTypeCode("hacc")

    @classproperty
    def PostAcuteCare(cls) -> "EpisodeOfCareTypeCode":
        """
        Post Acute Care
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareTypeCode("pac")

    @classproperty
    def PostCoordinatedDiabetes(cls) -> "EpisodeOfCareTypeCode":
        """
        Post coordinated diabetes program
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareTypeCode("diab")

    @classproperty
    def DrugAndAlcoholRehab(cls) -> "EpisodeOfCareTypeCode":
        """
        Drug and alcohol rehabilitation
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareTypeCode("da")

    @classproperty
    def CommunityBasedAgedCare(cls) -> "EpisodeOfCareTypeCode":
        """
        Community-based aged care
        """
        # noinspection PyCallingNonCallable
        return EpisodeOfCareTypeCode("cacp")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/episodeofcare-type
        """
        return "http://hl7.org/fhir/ValueSet/episodeofcare-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.666
        """
        return "2.16.840.1.113883.4.642.3.666"
