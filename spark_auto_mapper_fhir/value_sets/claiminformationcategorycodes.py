from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Claiminformationcategorycodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ClaiminformationcategorycodesValues:
    Information = Claiminformationcategorycodes("info")
    Discharge = Claiminformationcategorycodes("discharge")
    Onset = Claiminformationcategorycodes("onset")
    RelatedServices = Claiminformationcategorycodes("related")
    Exception = Claiminformationcategorycodes("exception")
    MaterialsForwarded = Claiminformationcategorycodes("material")
    Attachment = Claiminformationcategorycodes("attachment")
    MissingTooth = Claiminformationcategorycodes("missingtooth")
    Prosthesis = Claiminformationcategorycodes("prosthesis")
    Other = Claiminformationcategorycodes("other")
    Hospitalized = Claiminformationcategorycodes("hospitalized")
    Employmentimpacted = Claiminformationcategorycodes("employmentimpacted")
    ExternalCaause = Claiminformationcategorycodes("externalcause")
    PatientReasonForVisit = Claiminformationcategorycodes("patientreasonforvisit")