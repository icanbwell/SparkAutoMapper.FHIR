from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceDefinitionParameterGroup(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class DeviceDefinitionParameterGroupValues:
    HaemodynamicParameterGroup = DeviceDefinitionParameterGroup("haemodynamic")
    ECGParameterGroup = DeviceDefinitionParameterGroup("ecg")
    RespiratoryParameterGroup = DeviceDefinitionParameterGroup("respiratory")
    VentilationParameterGroup = DeviceDefinitionParameterGroup("ventilation")
    NeurologicalParameterGroup = DeviceDefinitionParameterGroup("neurological")
    DrugDeliveryParameterGroup = DeviceDefinitionParameterGroup("drug-delivery")
    FluidChemistryParameterGroup = DeviceDefinitionParameterGroup("fluid-chemistry")
    BloodChemistryParameterGroup = DeviceDefinitionParameterGroup("blood-chemistry")
    MiscellaneousParameterGroup = DeviceDefinitionParameterGroup("miscellaneous")