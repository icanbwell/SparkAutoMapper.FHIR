from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Fhirdevicestatus(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class FhirdevicestatusValues:
    Active = Fhirdevicestatus("active")
    Inactive = Fhirdevicestatus("inactive")
    EnteredInError = Fhirdevicestatus("entered-in-error")
    Unknown = Fhirdevicestatus("unknown")