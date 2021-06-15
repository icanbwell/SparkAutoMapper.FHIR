from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class EncounterDietCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-encounter-diet.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "EncounterDietCode"]) -> None:
            self.f: Callable[..., "EncounterDietCode"] = f

        def __get__(
            self, obj: Any, owner: Type["EncounterDietCode"]
        ) -> "EncounterDietCode":
            return self.f(owner)

    @classproperty
    def Vegetarian(cls) -> "EncounterDietCode":
        """
        Food without meat, poultry or seafood.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("vegetarian")

    @classproperty
    def DairyFree(cls) -> "EncounterDietCode":
        """
        Excludes dairy products.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("dairy-free")

    @classproperty
    def NutFree(cls) -> "EncounterDietCode":
        """
        Excludes ingredients containing nuts.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("nut-free")

    @classproperty
    def GlutenFree(cls) -> "EncounterDietCode":
        """
        Excludes ingredients containing gluten.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("gluten-free")

    @classproperty
    def Vegan(cls) -> "EncounterDietCode":
        """
        Food without meat, poultry, seafood, eggs, dairy products and other animal-derived substances.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("vegan")

    @classproperty
    def Halal(cls) -> "EncounterDietCode":
        """
        Foods that conform to Islamic law.
        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("halal")

    @classproperty
    def Kosher(cls) -> "EncounterDietCode":
        """
        Foods that conform to Jewish dietary law.

        """
        # noinspection PyCallingNonCallable
        return EncounterDietCode("kosher")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/encounter-diet
        """
        return "http://hl7.org/fhir/ValueSet/encounter-diet"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.255
        """
        return "2.16.840.1.113883.4.642.3.255"
