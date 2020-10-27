from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase


class Annotation(FhirComplexTypeBase):
    def __init__(self) -> None:
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        """
        super().__init__()
