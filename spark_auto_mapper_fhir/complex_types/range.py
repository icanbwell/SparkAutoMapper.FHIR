from typing import Optional

from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)


class Range(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        low: Optional[SimpleQuantity] = None,
        high: Optional[SimpleQuantity] = None,
    ) -> None:
        """
        Range Complex Type in FHIR
        https://www.hl7.org/fhir/datatypes.html#Range
        Set of values bounded by low and high
        + Rule: If present, low SHALL have a lower value than high


        :param low: Low limit
        :param high: High limit
        """
        super().__init__(id_=id_, extension=extension, low=low, high=high)
