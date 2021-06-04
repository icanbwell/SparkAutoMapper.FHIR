from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class BaseExtensionItem(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: str,
        valueString: Optional[FhirString] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        include_null_properties: bool = True,
    ) -> None:
        super().__init__(url=url, valueString=valueString, valueDateTime=valueDateTime)
        super().include_null_properties(include_null_properties=True)
