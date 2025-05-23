from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class IANATimezonesCode(GenericTypeCode):
    """
    IANATimezones
    From: http://hl7.org/fhir/ValueSet/timezones in valuesets.xml
        IANA Timezone Codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    https://www.iana.org/time-zones
    """
    codeset: FhirUri = "https://www.iana.org/time-zones"
