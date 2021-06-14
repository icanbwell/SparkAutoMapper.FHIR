from __future__ import annotations
from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class ${Class}(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        url: Optional[FhirUri] = None,
        valueCode: Optional[FhirValueSetBase] = None
    ) -> None:
        """
        ${Class} Extension type in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        """
        super().__init__(url=url or ${Class}.codeset, valueCode=valueCode)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "${codeset}"
