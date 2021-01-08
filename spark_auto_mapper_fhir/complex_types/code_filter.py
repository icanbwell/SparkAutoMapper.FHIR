from typing import Optional

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class CodeFilter(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        path: Optional[FhirString] = None,
        search_param: Optional[FhirString] = None,
        code: Optional[FhirList[Coding[FhirValueSetBase]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        CodeFilter Complex Type in FHIR
        https://www.hl7.org/fhir/element.html
        """
        super().__init__(
            id_=id_,
            path=path,
            search_param=search_param,
            code=code,
            extension=extension
        )
