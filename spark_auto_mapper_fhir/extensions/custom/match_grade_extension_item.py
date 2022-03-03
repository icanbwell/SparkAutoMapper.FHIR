from typing import Optional

from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.string import FhirString


# noinspection SpellCheckingInspection
class MatchGradeExtensionItem(NestedExtensionItem):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        url: str,
        valueString: Optional[FhirString] = None,
        valueDateTime: Optional[FhirDateTime] = None,
    ) -> None:
        super().__init__(
            id_=id_, url=url, valueString=valueString, valueDateTime=valueDateTime
        )
