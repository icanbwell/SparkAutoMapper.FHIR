from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.servicerequest import ServiceRequestSchema

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
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest

    # replaces (Reference)
    # Imports for References for replaces
    # requisition (Identifier)
    # status (RequestStatus)
    from spark_auto_mapper_fhir.value_sets.request_status import RequestStatusCode

    # intent (RequestIntent)
    from spark_auto_mapper_fhir.value_sets.request_intent import RequestIntentCode

    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.service_request_category_codes import (
        ServiceRequestCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
    # priority (RequestPriority)
    from spark_auto_mapper_fhir.value_sets.request_priority import RequestPriorityCode

    # doNotPerform (boolean)
    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.procedure_codes_snomedct_ import (
        ProcedureCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for code
    # orderDetail (CodeableConcept)
    # Import for CodeableConcept for orderDetail
    from spark_auto_mapper_fhir.value_sets.service_request_order_details_codes import (
        ServiceRequestOrderDetailsCodesCode,
    )

    # End Import for CodeableConcept for orderDetail
    # quantityQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # quantityRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # quantityRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.device import Device

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # occurrenceDateTime (dateTime)
    # occurrencePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # occurrenceTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # asNeededBoolean (boolean)
    # asNeededCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for asNeededCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for asNeededCodeableConcept
    # authoredOn (dateTime)
    # requester (Reference)
    # Imports for References for requester
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # performerType (CodeableConcept)
    # Import for CodeableConcept for performerType
    from spark_auto_mapper_fhir.value_sets.participant_roles import ParticipantRolesCode

    # End Import for CodeableConcept for performerType
    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

    # locationCode (CodeableConcept)
    # Import for CodeableConcept for locationCode
    from spark_auto_mapper_fhir.value_sets.service_delivery_location_role_type import (
        ServiceDeliveryLocationRoleType,
    )

    # End Import for CodeableConcept for locationCode
    # locationReference (Reference)
    # Imports for References for locationReference
    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.procedure_reason_codes import (
        ProcedureReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # insurance (Reference)
    # Imports for References for insurance
    from spark_auto_mapper_fhir.resources.coverage import Coverage
    from spark_auto_mapper_fhir.resources.claim_response import ClaimResponse

    # supportingInfo (Reference)
    # Imports for References for supportingInfo
    from spark_auto_mapper_fhir.resources.resource import Resource

    # specimen (Reference)
    # Imports for References for specimen
    from spark_auto_mapper_fhir.resources.specimen import Specimen

    # bodySite (CodeableConcept)
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # patientInstruction (string)
    # relevantHistory (Reference)
    # Imports for References for relevantHistory
    from spark_auto_mapper_fhir.resources.provenance import Provenance


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ServiceRequest(FhirResourceBase):
    """
    ServiceRequest
    servicerequest.xsd
        A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
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
        instantiatesCanonical: Optional[FhirList[FhirCanonical]] = None,
        instantiatesUri: Optional[FhirList[FhirUri]] = None,
        basedOn: Optional[
            FhirList[Reference[Union[CarePlan, ServiceRequest, MedicationRequest]]]
        ] = None,
        replaces: Optional[FhirList[Reference[ServiceRequest]]] = None,
        requisition: Optional[Identifier] = None,
        status: RequestStatusCode,
        intent: RequestIntentCode,
        category: Optional[
            FhirList[CodeableConcept[ServiceRequestCategoryCodesCode]]
        ] = None,
        priority: Optional[RequestPriorityCode] = None,
        doNotPerform: Optional[FhirBoolean] = None,
        code: Optional[CodeableConcept[ProcedureCodes_SNOMEDCT_Code]] = None,
        orderDetail: Optional[
            FhirList[CodeableConcept[ServiceRequestOrderDetailsCodesCode]]
        ] = None,
        quantityQuantity: Optional[Quantity] = None,
        quantityRatio: Optional[Ratio] = None,
        quantityRange: Optional[Range] = None,
        subject: Reference[Union[Patient, Group, Location, Device]],
        encounter: Optional[Reference[Encounter]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrencePeriod: Optional[Period] = None,
        occurrenceTiming: Optional[Timing] = None,
        asNeededBoolean: Optional[FhirBoolean] = None,
        asNeededCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
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
        performerType: Optional[CodeableConcept[ParticipantRolesCode]] = None,
        performer: Optional[
            FhirList[
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
            ]
        ] = None,
        locationCode: Optional[
            FhirList[CodeableConcept[ServiceDeliveryLocationRoleType]]
        ] = None,
        locationReference: Optional[FhirList[Reference[Location]]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[ProcedureReasonCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        insurance: Optional[FhirList[Reference[Union[Coverage, ClaimResponse]]]] = None,
        supportingInfo: Optional[FhirList[Reference[Resource]]] = None,
        specimen: Optional[FhirList[Reference[Specimen]]] = None,
        bodySite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        patientInstruction: Optional[FhirString] = None,
        relevantHistory: Optional[FhirList[Reference[Provenance]]] = None,
    ) -> None:
        """
            A record of a request for service such as diagnostic investigations,
        treatments, or operations to be performed.
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
            :param identifier: Identifiers assigned to this order instance by the orderer and/or the receiver
        and/or order fulfiller.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
        definition that is adhered to in whole or in part by this ServiceRequest.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
        other definition that is adhered to in whole or in part by this
        ServiceRequest.
            :param basedOn: Plan/proposal/order fulfilled by this request.
            :param replaces: The request takes the place of the referenced completed or terminated
        request(s).
            :param requisition: A shared identifier common to all service requests that were authorized more
        or less simultaneously by a single author, representing the composite or group
        identifier.
            :param status: The status of the order.
            :param intent: Whether the request is a proposal, plan, an original order or a reflex order.
            :param category: A code that classifies the service for searching, sorting and display purposes
        (e.g. "Surgical Procedure").
            :param priority: Indicates how quickly the ServiceRequest should be addressed with respect to
        other requests.
            :param doNotPerform: Set this to true if the record is saying that the service/procedure should NOT
        be performed.
            :param code: A code that identifies a particular service (i.e., procedure, diagnostic
        investigation, or panel of investigations) that have been requested.
            :param orderDetail: Additional details and instructions about the how the services are to be
        delivered.   For example, and order for a urinary catheter may have an order
        detail for an external or indwelling catheter, or an order for a bandage may
        require additional instructions specifying how the bandage should be applied.
            :param quantityQuantity: None
            :param quantityRatio: None
            :param quantityRange: None
            :param subject: On whom or what the service is to be performed. This is usually a human
        patient, but can also be requested on animals, groups of humans or animals,
        devices such as dialysis machines, or even locations (typically for
        environmental scans).
            :param encounter: An encounter that provides additional information about the healthcare context
        in which this request is made.
            :param occurrenceDateTime: None
            :param occurrencePeriod: None
            :param occurrenceTiming: None
            :param asNeededBoolean: None
            :param asNeededCodeableConcept: None
            :param authoredOn: When the request transitioned to being actionable.
            :param requester: The individual who initiated the request and has responsibility for its
        activation.
            :param performerType: Desired type of performer for doing the requested service.
            :param performer: The desired performer for doing the requested service.  For example, the
        surgeon, dermatopathologist, endoscopist, etc.
            :param locationCode: The preferred location(s) where the procedure should actually happen in coded
        or free text form. E.g. at home or nursing day care center.
            :param locationReference: A reference to the the preferred location(s) where the procedure should
        actually happen. E.g. at home or nursing day care center.
            :param reasonCode: An explanation or justification for why this service is being requested in
        coded or textual form.   This is often for billing purposes.  May relate to
        the resources referred to in `supportingInfo`.
            :param reasonReference: Indicates another resource that provides a justification for why this service
        is being requested.   May relate to the resources referred to in
        `supportingInfo`.
            :param insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
        determinations that may be needed for delivering the requested service.
            :param supportingInfo: Additional clinical information about the patient or specimen that may
        influence the services or their interpretations.     This information includes
        diagnosis, clinical findings and other observations.  In laboratory ordering
        these are typically referred to as "ask at order entry questions (AOEs)".
        This includes observations explicitly requested by the producer (filler) to
        provide context or supporting information needed to complete the order. For
        example,  reporting the amount of inspired oxygen for blood gas measurements.
            :param specimen: One or more specimens that the laboratory procedure will use.
            :param bodySite: Anatomic location where the procedure should be performed. This is the target
        site.
            :param note: Any other notes and comments made about the service request. For example,
        internal billing notes.
            :param patientInstruction: Instructions in terms that are understood by the patient or consumer.
            :param relevantHistory: Key events in the history of the request.
        """
        super().__init__(
            resourceType="ServiceRequest",
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
            replaces=replaces,
            requisition=requisition,
            status=status,
            intent=intent,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            code=code,
            orderDetail=orderDetail,
            quantityQuantity=quantityQuantity,
            quantityRatio=quantityRatio,
            quantityRange=quantityRange,
            subject=subject,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            asNeededBoolean=asNeededBoolean,
            asNeededCodeableConcept=asNeededCodeableConcept,
            authoredOn=authoredOn,
            requester=requester,
            performerType=performerType,
            performer=performer,
            locationCode=locationCode,
            locationReference=locationReference,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            supportingInfo=supportingInfo,
            specimen=specimen,
            bodySite=bodySite,
            note=note,
            patientInstruction=patientInstruction,
            relevantHistory=relevantHistory,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ServiceRequestSchema.get_schema(include_extension=include_extension)
