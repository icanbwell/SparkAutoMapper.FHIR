from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase


class Annotation(FhirComplexTypeBase):
    def __init__(self, id_: Optional[FhirId] = None) -> None:
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        """
        super().__init__(id_=id_)
