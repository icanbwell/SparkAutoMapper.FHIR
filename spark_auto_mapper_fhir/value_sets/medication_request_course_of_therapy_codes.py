from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationRequestCourseOfTherapyCodesCode(GenericTypeCode):
    """
    medicationRequest Course of Therapy Codes
    From: http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy in valuesets.xml
        MedicationRequest Course of Therapy Codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy"
    )


class MedicationRequestCourseOfTherapyCodesCodeValues:
    """
    A medication which is expected to be continued beyond the present order and
    which the patient should be assumed to be taking unless explicitly stopped.
    From: http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy in valuesets.xml
    """

    ContinuousLongTermTherapy = MedicationRequestCourseOfTherapyCodesCode("continuous")
    """
    A medication which the patient is only expected to consume for the duration of
    the current order and which is not expected to be renewed.
    From: http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy in valuesets.xml
    """
    ShortCourse_acute_Therapy = MedicationRequestCourseOfTherapyCodesCode("acute")
    """
    A medication which is expected to be used on a part time basis at certain
    times of the year
    From: http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy in valuesets.xml
    """
    Seasonal = MedicationRequestCourseOfTherapyCodesCode("seasonal")
