from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.task import TaskSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # instantiatesCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # instantiatesUri (uri)
    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource

    # groupIdentifier (Identifier)
    # partOf (Reference)
    # Imports for References for partOf
    # status (TaskStatus)
    from spark_auto_mapper_fhir.value_sets.task_status import TaskStatusCode

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for statusReason
    # businessStatus (CodeableConcept)
    # Import for CodeableConcept for businessStatus
    # End Import for CodeableConcept for businessStatus
    # intent (TaskIntent)
    from spark_auto_mapper_fhir.value_sets.task_intent import TaskIntentCode

    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.task_code import TaskCodeCode

    # End Import for CodeableConcept for code
    # description (string)
    # focus (Reference)
    # Imports for References for focus
    # for_ (Reference)
    # Imports for References for for_
    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # executionPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # authoredOn (dateTime)
    # lastModified (dateTime)
    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # performerType (CodeableConcept)
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.procedure_performer_role_codes import (
        ProcedurePerformerRoleCodesCode,
    )

    # End Import for CodeableConcept for performerType
    # owner (Reference)
    # Imports for References for owner
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    # insurance (Reference)
    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # relevantHistory (Reference)
    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance

    # restriction (Task.Restriction)
    from spark_auto_mapper_fhir.backbone_elements.task_restriction import (
        TaskRestriction,
    )

    # input (Task.Input)
    from spark_auto_mapper_fhir.backbone_elements.task_input import TaskInput

    # output (Task.Output)
    from spark_auto_mapper_fhir.backbone_elements.task_output import TaskOutput


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Task(FhirResourceBase):
    """
    Task
    task.xsd
        A task to be performed.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        instantiatesCanonical: Optional[FhirCanonical] = None,
        instantiatesUri: Optional[FhirUri] = None,
        basedOn: Optional[FhirList[Reference[Resource]]] = None,
        groupIdentifier: Optional[Identifier] = None,
        partOf: Optional[FhirList[Reference[Task]]] = None,
        status: TaskStatusCode,
        statusReason: Optional[CodeableConcept[GenericTypeCode]] = None,
        businessStatus: Optional[CodeableConcept[GenericTypeCode]] = None,
        intent: TaskIntentCode,
        priority: Optional[RequestPriorityCode] = None,
        code: Optional[CodeableConcept[TaskCodeCode]] = None,
        description: Optional[FhirString] = None,
        focus: Optional[Reference[Resource]] = None,
        for_: Optional[Reference[Resource]] = None,
        encounter: Optional[Reference[Encounter]] = None,
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
        performerType: Optional[
            FhirList[CodeableConcept[ProcedurePerformerRoleCodesCode]]
        ] = None,
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
        location: Optional[Reference[Location]] = None,
        reasonCode: Optional[CodeableConcept[GenericTypeCode]] = None,
        reasonReference: Optional[Reference[Resource]] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage, ClaimResponse]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        relevantHistory: Optional[FhirList[Reference[Provenance]]] = None,
        restriction: Optional[TaskRestriction] = None,
        input: Optional[FhirList[TaskInput]] = None,
        output: Optional[FhirList[TaskOutput]] = None,
    ) -> None:
        """
            A task to be performed.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
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
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
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
