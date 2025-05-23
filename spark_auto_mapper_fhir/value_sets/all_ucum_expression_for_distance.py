from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AllUCUMExpressionForDistanceCode(GenericTypeCode):
    """
    AllUCUMExpressionForDistance
    From: http://hl7.org/fhir/ValueSet/all-distance-units in valuesets.xml
        Unified Code for Units of Measure (UCUM). This value set includes all UCUM
    codes for units of length
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://unitsofmeasure.org
    """
    codeset: FhirUri = "http://unitsofmeasure.org"
