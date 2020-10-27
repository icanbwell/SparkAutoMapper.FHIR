from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.fhir_extension_base import FhirExtensionBase
from spark_auto_mapper_fhir.extensions.us_core.race_item import RaceItem
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class Race(FhirExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        extension: Optional[FhirList[RaceItem]] = None
    ) -> None:
        """
        Extension type in FHIR
        """
        super().__init__(url=url or Race.codeset, extension=extension)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
