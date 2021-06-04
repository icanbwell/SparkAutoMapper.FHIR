from typing import Optional

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)
from spark_auto_mapper_fhir.valuesets.sort_direction import SortDirectionCode


class Sort(FhirComplexTypeBase):
    def __init__(
        self,
        path: FhirString,
        direction: SortDirectionCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        Sort Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes-definitions.html#DataRequirement.sort
        Order of the results


        :param path: The name of the attribute to perform the sort
        :param direction: 	ascending | descending
        """
        super().__init__(id_=id_, extension=extension, path=path, direction=direction)
