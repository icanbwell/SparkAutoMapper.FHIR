from typing import Optional

from spark_auto_mapper_fhir.complex_types.code_filter import CodeFilter
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.valuesets.all_types import FhirAllTypesCode


class DataRequirement(FhirComplexTypeBase):
    def __init__(
        self,
        type_: FhirAllTypesCode,
        id_: Optional[FhirId] = None,
        code_filter: Optional[FhirList[CodeFilter]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        DataRequirement Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#DataRequirement
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            code_filter=code_filter,
        )
