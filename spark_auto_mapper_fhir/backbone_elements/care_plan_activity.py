from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for outcomeReference
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reference
    from spark_auto_mapper_fhir.resources.appointment import Appointment
    from spark_auto_mapper_fhir.resources.communication_request import (
        CommunicationRequest,
    )
    from spark_auto_mapper_fhir.resources.device_request import DeviceRequest
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.nutrition_order import NutritionOrder
    from spark_auto_mapper_fhir.resources.task import Task
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.resources.vision_prescription import VisionPrescription
    from spark_auto_mapper_fhir.resources.request_group import RequestGroup
    from spark_auto_mapper_fhir.backbone_elements.care_plan_detail import CarePlanDetail


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CarePlanActivity(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        outcomeCodeableConcept: Optional[FhirList[CodeableConcept]] = None,
        outcomeReference: Optional[FhirList[Reference[Union[Resource]]]] = None,
        progress: Optional[FhirList[Annotation]] = None,
        reference: Optional[
            Reference[
                Union[
                    Appointment,
                    CommunicationRequest,
                    DeviceRequest,
                    MedicationRequest,
                    NutritionOrder,
                    Task,
                    ServiceRequest,
                    VisionPrescription,
                    RequestGroup,
                ]
            ]
        ] = None,
        detail: Optional[CarePlanDetail] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param outcomeCodeableConcept: Identifies the outcome at the point when the status of the activity is
        assessed.  For example, the outcome of an education activity could be patient
        understands (or not).
            :param outcomeReference: Details of the outcome or action resulting from the activity.  The reference
        to an "event" resource, such as Procedure or Encounter or Observation, is the
        result/outcome of the activity itself.  The activity can be conveyed using
        CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference
        to a “request” resource).
            :param progress: Notes about the adherence/status/progress of the activity.
            :param reference: The details of the proposed activity represented in a specific resource.
            :param detail: A simple summary of a planned activity suitable for a general care plan system
        (e.g. form driven) that doesn't know about specific resources such as
        procedure etc.
        """
        super().__init__(
            resourceType="CarePlanActivity",
            id_=id_,
            meta=meta,
            extension=extension,
            outcomeCodeableConcept=outcomeCodeableConcept,
            outcomeReference=outcomeReference,
            progress=progress,
            reference=reference,
            detail=detail,
        )