from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ServiceRequestOrderDetailsCodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ServiceRequestOrderDetailsCodesValues:
    ContinuousPositiveAirwayPressureVentilationTreatment_regime_therapy_ = (
        ServiceRequestOrderDetailsCodes("47545007")
    )
    PressureControlledVentilation_procedure_ = ServiceRequestOrderDetailsCodes(
        "286812008"
    )
    PatientTriggeredInspiratoryAssistance_procedure_ = ServiceRequestOrderDetailsCodes(
        "243144002"
    )
    AssistedControlledMandatoryVentilation_procedure_ = ServiceRequestOrderDetailsCodes(
        "243150007"
    )
    SynchronizedIntermittentMandatoryVentilation_procedure_ = (
        ServiceRequestOrderDetailsCodes("59427005")
    )