from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicationrequest import MedicationRequestSchema

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

    # status (medicationrequest Status)
    from spark_auto_mapper_fhir.value_sets.medicationrequest_status import (
        MedicationrequestStatusCode,
    )

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.medication_request_status_reason_codes import (
        MedicationRequestStatusReasonCodesCode,
    )

    # End Import for CodeableConcept for statusReason
    # intent (medicationRequest Intent)
    from spark_auto_mapper_fhir.value_sets.medication_request_intent import (
        MedicationRequestIntentCode,
    )

    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.medication_request_category_codes import (
        MedicationRequestCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # doNotPerform (boolean)
    # reportedBoolean (boolean)
    # reportedReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reportedReference
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # medicationCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for medicationCodeableConcept
    from spark_auto_mapper_fhir.value_sets.snomedct_medication_codes import (
        SNOMEDCTMedicationCodesCode,
    )

    # End Import for CodeableConcept for medicationCodeableConcept
    # medicationReference (Reference)
    # Imports for References for medicationReference
    from spark_auto_mapper_fhir.resources.medication import Medication

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.group import Group

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # supportingInformation (Reference)
    # Imports for References for supportingInformation
    from spark_auto_mapper_fhir.resources.resource import Resource

    # authoredOn (dateTime)
    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.device import Device

    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.care_team import CareTeam

    # performerType (CodeableConcept)
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.procedure_performer_role_codes import (
        ProcedurePerformerRoleCodesCode,
    )

    # End Import for CodeableConcept for performerType
    # recorder (Reference)
    # Imports for References for recorder
    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.condition_or__problem_or__diagnosis_codes import (
        Condition_or_Problem_or_DiagnosisCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation

    # instantiatesCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # instantiatesUri (uri)
    # basedOn (Reference)
    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.resources.immunization_recommendation import (
        ImmunizationRecommendation,
    )

    # groupIdentifier (Identifier)
    # courseOfTherapyType (CodeableConcept)
    # Import for CodeableConcept for courseOfTherapyType
    from spark_auto_mapper_fhir.value_sets.medication_request_course_of_therapy_codes import (
        MedicationRequestCourseOfTherapyCodesCode,
    )

    # End Import for CodeableConcept for courseOfTherapyType
    # insurance (Reference)
    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # dosageInstruction (Dosage)
    from spark_auto_mapper_fhir.backbone_elements.dosage import Dosage

    # dispenseRequest (MedicationRequest.DispenseRequest)
    from spark_auto_mapper_fhir.backbone_elements.medication_request_dispense_request import (
        MedicationRequestDispenseRequest,
    )

    # substitution (MedicationRequest.Substitution)
    from spark_auto_mapper_fhir.backbone_elements.medication_request_substitution import (
        MedicationRequestSubstitution,
    )

    # priorPrescription (Reference)
    # Imports for References for priorPrescription
    # detectedIssue (Reference)
    # Imports for References for detectedIssue
    from spark_auto_mapper_fhir.resources.detected_issue import DetectedIssue

    # eventHistory (Reference)
    # Imports for References for eventHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationRequest(FhirResourceBase):
    """
    MedicationRequest
    medicationrequest.xsd
        An order or request for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
    to generalize the use across inpatient and outpatient settings, including care
    plans, etc., and to harmonize with workflow patterns.
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
        status: MedicationrequestStatusCode,
        statusReason: Optional[
            CodeableConcept[MedicationRequestStatusReasonCodesCode]
        ] = None,
        intent: MedicationRequestIntentCode,
        category: Optional[
            FhirList[CodeableConcept[MedicationRequestCategoryCodesCode]]
        ] = None,
        priority: Optional[RequestPriorityCode] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        reportedBoolean: Optional[FhirBoolean] = None,
        reportedReference: Optional[
            Reference[
                Union[
                    Patient, Practitioner, PractitionerRole, RelatedPerson, Organization
                ]
            ]
        ] = None,
        medicationCodeableConcept: Optional[
            CodeableConcept[SNOMEDCTMedicationCodesCode]
        ] = None,
        medicationReference: Optional[Reference[Medication]] = None,
        subject: Reference[Union[Patient, Group]],
        encounter: Optional[Reference[Encounter]] = None,
        supportingInformation: Optional[FhirList[Reference[Resource]]] = None,
        authoredOn: Optional[FhirDateTime] = None,
        requester: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    Patient,
                    RelatedPerson,
                    Device,
                ]
            ]
        ] = None,
        performer: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Organization,
                    Patient,
                    Device,
                    RelatedPerson,
                    CareTeam,
                ]
            ]
        ] = None,
        performerType: Optional[
            CodeableConcept[ProcedurePerformerRoleCodesCode]
        ] = None,
        recorder: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[Condition_or_Problem_or_DiagnosisCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[Reference[Union[Condition, Observation]]]
        ] = None,
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        basedOn: Optional[
            FhirList[
                Reference[
                    Union[
                        CarePlan,
                        MedicationRequest,
                        ServiceRequest,
                        ImmunizationRecommendation,
                    ]
                ]
            ]
        ] = None,
        groupIdentifier: Optional[Identifier] = None,
        courseOfTherapyType: Optional[
            CodeableConcept[MedicationRequestCourseOfTherapyCodesCode]
        ] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage, ClaimResponse]]]] = None,
        note: Optional[FhirList[Annotation]] = None,
        dosageInstruction: Optional[FhirList[Dosage]] = None,
        dispenseRequest: Optional[MedicationRequestDispenseRequest] = None,
        substitution: Optional[MedicationRequestSubstitution] = None,
        priorPrescription: Optional[Reference[MedicationRequest]] = None,
        detectedIssue: Optional[FhirList[Reference[DetectedIssue]]] = None,
        eventHistory: Optional[FhirList[Reference[Provenance]]] = None,
    ) -> None:
        """
            An order or request for both supply of the medication and the instructions for
        administration of the medication to a patient. The resource is called
        "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
        to generalize the use across inpatient and outpatient settings, including care
        plans, etc., and to harmonize with workflow patterns.
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
            :param identifier: Identifiers associated with this medication request that are defined by
        business processes and/or used to refer to it when a direct URL reference to
        the resource itself is not appropriate. They are business identifiers assigned
        to this resource by the performer or other systems and remain constant as the
        resource is updated and propagates from server to server.
            :param status: A code specifying the current state of the order.  Generally, this will be
        active or completed state.
            :param statusReason: Captures the reason for the current state of the MedicationRequest.
            :param intent: Whether the request is a proposal, plan, or an original order.
            :param category: Indicates the type of medication request (for example, where the medication is
        expected to be consumed or administered (i.e. inpatient or outpatient)).
            :param priority: Indicates how quickly the Medication Request should be addressed with respect
        to other requests.
            :param doNotPerform: If true indicates that the provider is asking for the medication request not
        to occur.
            :param reportedBoolean: None
            :param reportedReference: None
            :param medicationCodeableConcept: None
            :param medicationReference: None
            :param subject: A link to a resource representing the person or set of individuals to whom the
        medication will be given.
            :param encounter: The Encounter during which this [x] was created or to which the creation of
        this record is tightly associated.
            :param supportingInformation: Include additional information (for example, patient height and weight) that
        supports the ordering of the medication.
            :param authoredOn: The date (and perhaps time) when the prescription was initially written or
        authored on.
            :param requester: The individual, organization, or device that initiated the request and has
        responsibility for its activation.
            :param performer: The specified desired performer of the medication treatment (e.g. the
        performer of the medication administration).
            :param performerType: Indicates the type of performer of the administration of the medication.
            :param recorder: The person who entered the order on behalf of another individual for example
        in the case of a verbal or a telephone order.
            :param reasonCode: The reason or the indication for ordering or not ordering the medication.
            :param reasonReference: Condition or observation that supports why the medication was ordered.
            :param instantiatesCanonical: The URL pointing to a protocol, guideline, orderset, or other definition that
        is adhered to in whole or in part by this MedicationRequest.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this
        MedicationRequest.
            :param basedOn: A plan or request that is fulfilled in whole or in part by this medication
        request.
            :param groupIdentifier: A shared identifier common to all requests that were authorized more or less
        simultaneously by a single author, representing the identifier of the
        requisition or prescription.
            :param courseOfTherapyType: The description of the overall patte3rn of the administration of the
        medication to the patient.
            :param insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
        determinations that may be required for delivering the requested service.
            :param note: Extra information about the prescription that could not be conveyed by the
        other attributes.
            :param dosageInstruction: Indicates how the medication is to be used by the patient.
            :param dispenseRequest: Indicates the specific details for the dispense or medication supply part of a
        medication request (also known as a Medication Prescription or Medication
        Order).  Note that this information is not always sent with the order.  There
        may be in some settings (e.g. hospitals) institutional or system support for
        completing the dispense details in the pharmacy department.
            :param substitution: Indicates whether or not substitution can or should be part of the dispense.
        In some cases, substitution must happen, in other cases substitution must not
        happen. This block explains the prescriber's intent. If nothing is specified
        substitution may be done.
            :param priorPrescription: A link to a resource representing an earlier order related order or
        prescription.
            :param detectedIssue: Indicates an actual or potential clinical issue with or between one or more
        active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
        duplicate therapy, dosage alert etc.
            :param eventHistory: Links to Provenance records for past versions of this resource or fulfilling
        request or event resources that identify key state transitions or updates that
        are likely to be relevant to a user looking at the current version of the
        resource.
        """
        super().__init__(
            resourceType="MedicationRequest",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            statusReason=statusReason,
            intent=intent,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            reportedBoolean=reportedBoolean,
            reportedReference=reportedReference,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            encounter=encounter,
            supportingInformation=supportingInformation,
            authoredOn=authoredOn,
            requester=requester,
            performer=performer,
            performerType=performerType,
            recorder=recorder,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            groupIdentifier=groupIdentifier,
            courseOfTherapyType=courseOfTherapyType,
            insurance=insurance,
            note=note,
            dosageInstruction=dosageInstruction,
            dispenseRequest=dispenseRequest,
            substitution=substitution,
            priorPrescription=priorPrescription,
            detectedIssue=detectedIssue,
            eventHistory=eventHistory,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicationRequestSchema.get_schema(include_extension=include_extension)
