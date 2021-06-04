from typing import Optional

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)


class Ratio(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        numerator: Optional[Quantity] = None,
        denominator: Optional[Quantity] = None,
    ) -> None:
        """
        Ratio Complex Type in FHIR
        https://www.hl7.org/fhir/datatypes.html#Ratio
        A ratio of two Quantity values - a numerator and a denominator
        + Rule: Numerator and denominator SHALL both be present, or both are absent. If both are absent,
                there SHALL be some extension present
        """
        super().__init__(
            id_=id_, extension=extension, numerator=numerator, denominator=denominator
        )
