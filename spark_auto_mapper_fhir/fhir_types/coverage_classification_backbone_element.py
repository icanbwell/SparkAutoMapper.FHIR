from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.coverage_class import FhirCoverageClassCode
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirCoverageClassificationBackboneElement(FhirResourceBase):
    @classmethod
    def map(
        cls,
        type_: FhirCodeableConcept[FhirCoverageClassCode],
        value: FhirString,
        name: Optional[FhirString] = None
    ) -> 'FhirCoverageClassificationBackboneElement':
        """
        CoverageClassificationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.class
        Additional coverage classifications

        :param type_: Type of class such as 'group' or 'plan'. https://hl7.org/FHIR/valueset-coverage-class.html
        :param value: Value associated with the type
        :param name: Human readable description of the type and value
        """
        return FhirCoverageClassificationBackboneElement(
            type_=type_, value=value, name=name
        )
