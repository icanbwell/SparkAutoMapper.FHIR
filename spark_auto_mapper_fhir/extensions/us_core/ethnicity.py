from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.extensions.us_core.ethnicity_item import EthnicityItem
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class Ethnicity(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        extension: Optional[FhirList[EthnicityItem]] = None,
    ) -> None:
        """
        Extension type in FHIR
        """
        super().__init__(url=url or Ethnicity.codeset, extension=extension)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
