from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class VaccineAdministeredValueSetCode(GenericTypeCode):
    """
    VaccineAdministeredValueSet
    From: http://hl7.org/fhir/ValueSet/vaccine-code in valuesets.xml
        This identifies the vaccine substance administered - CVX codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/sid/cvx
    """
    codeset_cvx: FhirUri = "http://hl7.org/fhir/sid/cvx"
    """
    urn:oid:1.2.36.1.2001.1005.17
    """
    codeset_urn_oid_1_2_36_1_2001_1005_17: FhirUri = "urn:oid:1.2.36.1.2001.1005.17"
