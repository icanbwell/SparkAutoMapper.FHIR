from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.coverage_class import CoverageClassCode
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class CoverageClassificationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        type_: CodeableConcept[CoverageClassCode],
        value: FhirString,
        name: Optional[FhirString] = None
    ):
        """
        CoverageClassificationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.class
        Additional coverage classifications

        :param type_: Type of class such as 'group' or 'plan'. https://hl7.org/FHIR/valueset-coverage-class.html
        :param value: Value associated with the type
        :param name: Human readable description of the type and value
        """
        super().__init__(type_=type_, value=value, name=name)
