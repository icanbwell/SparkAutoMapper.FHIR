from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Goalstatusreason(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class GoalstatusreasonValues:
    Surgery = Goalstatusreason("surgery")
    LifeEvent = Goalstatusreason("life-event")
    Replaced = Goalstatusreason("replaced")
    PatientRequest = Goalstatusreason("patient-request")
    GoalNotAttainableTemporarily = Goalstatusreason("temp-not-attainable")
    GoalNotAttainablePermanently = Goalstatusreason("permanent-not-attainable")
    FinancialReason = Goalstatusreason("financial-barrier")
    LackOfTransportation = Goalstatusreason("lack-of-transportation")
    LackOfSocialSupport = Goalstatusreason("lack-of-social-support")