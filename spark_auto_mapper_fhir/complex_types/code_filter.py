from typing import Optional

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class CodeFilter(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        path: Optional[FhirString] = None,
        search_param: Optional[FhirString] = None,
        valueSet: Optional[FhirCanonical] = None,
        code: Optional[FhirList[Coding[FhirValueSetBase]]] = None,
    ) -> None:
        """
        CodeFilter Complex Type in FHIR
        https://www.hl7.org/fhir/element.html
        What codes are expected
        + Rule: Either a path or a searchParam must be provided, but not both

        :param path: A code-valued attribute to filter on
        :param search_param: A coded (token) parameter to search on
        :param valueSet: Valueset for the filter
        :param code: What code is expected
        """
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            search_param=search_param,
            valueSet=valueSet,
            code=code,
        )
