from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.task import TaskSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.canonical import canonical
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for partOf
    from spark_auto_mapper_fhir.complex_types.task_status import TaskStatus
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.complex_types.task_status_reason import TaskStatusReason
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for businessStatus
    from spark_auto_mapper_fhir.complex_types.task_business_status import (
        TaskBusinessStatus,
    )
    from spark_auto_mapper_fhir.complex_types.task_intent import TaskIntent
    from spark_auto_mapper_fhir.complex_types.request_priority import RequestPriority
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.complex_types.task_code import TaskCode
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for focus
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.complex_types.task_performer_type import (
        TaskPerformerType,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for owner
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.complex_types.task_reason import TaskReason
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance
    from spark_auto_mapper_fhir.backbone_elements.task_restriction import (
        TaskRestriction,
    )
    from spark_auto_mapper_fhir.backbone_elements.task_input import TaskInput
    from spark_auto_mapper_fhir.backbone_elements.task_output import TaskOutput


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Task(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[canonical] = None,
        instantiatesUri: Optional[uri] = None,
        basedOn: Optional[FhirList[Reference[Union[Resource]]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        partOf: Optional[FhirList[Reference[Union[Task]]]] = None,
        status: TaskStatus,
        statusReason: Optional[CodeableConcept[TaskStatusReason]] = None,
        businessStatus: Optional[CodeableConcept[TaskBusinessStatus]] = None,
        intent: TaskIntent,
        priority: Optional[RequestPriority] = None,
        code: Optional[CodeableConcept[TaskCode]] = None,
        description: Optional[FhirString] = None,
        focus: Optional[Reference[Union[Resource]]] = None,
        for_: Optional[Reference] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        executionPeriod: Optional[Period] = None,
        authoredOn: Optional[FhirDateTime] = None,
        lastModified: Optional[FhirDateTime] = None,
        requester: Optional[
            Reference[
                Union[
                    Device,
                    Organization,
                    Patient,
                    Practitioner,
                    PractitionerRole,
                    RelatedPerson,
                ]
            ]
        ] = None,
        performerType: Optional[FhirList[CodeableConcept[TaskPerformerType]]] = None,
        owner: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    CareTeam,
                    HealthcareService,
                    Patient,
                    Device,
                    RelatedPerson,
                ]
            ]
        ] = None,
        location: Optional[Reference[Union[Location]]] = None,
        reasonCode: Optional[CodeableConcept[TaskReason]] = None,
        reasonReference: Optional[Reference[Union[Resource]]] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage, ClaimResponse]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        relevantHistory: Optional[FhirList[Reference[Union[Provenance]]]] = None,
        restriction: Optional[TaskRestriction] = None,
        input: Optional[FhirList[TaskInput]] = None,
        output: Optional[FhirList[TaskOutput]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: The business identifier for this task.
            :param instantiatesCanonical: The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this Task.
            :param instantiatesUri: The URL pointing to an *externally* maintained  protocol, guideline, orderset
        or other definition that is adhered to in whole or in part by this Task.
            :param basedOn: BasedOn refers to a higher-level authorization that triggered the creation of
        the task.  It references a "request" resource such as a ServiceRequest,
        MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the
        "request" resource the task is seeking to fulfill.  This latter resource is
        referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a
        task is created to fulfill a procedureRequest ( = FocusOn ) to collect a
        specimen from a patient.
            :param groupIdentifier: An identifier that links together multiple tasks and other requests that were
        created in the same context.
            :param partOf: Task that this particular task is part of.
            :param status: The current status of the task.
            :param statusReason: An explanation as to why this task is held, failed, was refused, etc.
            :param businessStatus: Contains business-specific nuances of the business state.
            :param intent: Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs
        this a proposed task, a planned task, an actionable task, etc.
            :param priority: Indicates how quickly the Task should be addressed with respect to other
        requests.
            :param code: A name or code (or both) briefly describing what the task involves.
            :param description: A free-text description of what is to be performed.
            :param focus: The request being actioned or the resource being manipulated by this task.
            :param for_: The entity who benefits from the performance of the service specified in the
        task (e.g., the patient).
            :param encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
        during which this task was created.
            :param executionPeriod: Identifies the time action was first taken against the task (start) and/or the
        time final action was taken against the task prior to marking it as completed
        (end).
            :param authoredOn: The date and time this task was created.
            :param lastModified: The date and time of last modification to this task.
            :param requester: The creator of the task.
            :param performerType: The kind of participant that should perform the task.
            :param owner: Individual organization or Device currently responsible for task execution.
            :param location: Principal physical location where the this task is performed.
            :param reasonCode: A description or code indicating why this task needs to be performed.
            :param reasonReference: A resource reference indicating why this task needs to be performed.
            :param insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
        determinations that may be relevant to the Task.
            :param note: Free-text information captured about the task as it progresses.
            :param relevantHistory: Links to Provenance records for past versions of this Task that identify key
        state transitions or updates that are likely to be relevant to a user looking
        at the current version of the task.
            :param restriction: If the Task.focus is a request resource and the task is seeking fulfillment
        (i.e. is asking for the request to be actioned), this element identifies any
        limitations on what parts of the referenced request should be actioned.
            :param input: Additional information that may be needed in the execution of the task.
            :param output: Outputs produced by the Task.
        """
        super().__init__(
            resourceType="Task",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            groupIdentifier=groupIdentifier,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            businessStatus=businessStatus,
            intent=intent,
            priority=priority,
            code=code,
            description=description,
            focus=focus,
            for_=for_,
            encounter=encounter,
            executionPeriod=executionPeriod,
            authoredOn=authoredOn,
            lastModified=lastModified,
            requester=requester,
            performerType=performerType,
            owner=owner,
            location=location,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            note=note,
            relevantHistory=relevantHistory,
            restriction=restriction,
            input=input,
            output=output,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return TaskSchema.get_schema(include_extension=include_extension)