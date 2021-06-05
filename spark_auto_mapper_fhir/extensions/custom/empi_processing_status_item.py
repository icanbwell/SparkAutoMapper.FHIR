from typing import Optional

from spark_auto_mapper_fhir.extensions.custom.base_extension_item import (
    BaseExtensionItem,
)
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.string import FhirString


# noinspection SpellCheckingInspection
class EmpiProcessingStatusExtensionItem(BaseExtensionItem):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: str,
        valueString: Optional[FhirString] = None,
        valueDateTime: Optional[FhirDateTime] = None,
    ) -> None:
        super().__init__(url=url, valueString=valueString, valueDateTime=valueDateTime)
