from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Servicerequestcategorycodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ServicerequestcategorycodesValues:
    LaboratoryProcedure = Servicerequestcategorycodes("108252007")
    Imaging = Servicerequestcategorycodes("363679005")
    Counselling = Servicerequestcategorycodes("409063005")
    Education = Servicerequestcategorycodes("409073007")
    SurgicalProcedure = Servicerequestcategorycodes("387713003")