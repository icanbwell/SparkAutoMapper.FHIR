from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CarePlanActivityStatus(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class CarePlanActivityStatusValues:
    NotStarted = CarePlanActivityStatus("not-started")
    Scheduled = CarePlanActivityStatus("scheduled")
    InProgress = CarePlanActivityStatus("in-progress")
    OnHold = CarePlanActivityStatus("on-hold")
    Completed = CarePlanActivityStatus("completed")
    Cancelled = CarePlanActivityStatus("cancelled")
    Unknown = CarePlanActivityStatus("unknown")
    EnteredInError = CarePlanActivityStatus("entered-in-error")