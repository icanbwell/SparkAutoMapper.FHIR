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
from spark_fhir_schemas.r4.resources.procedure import ProcedureSchema

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
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # partOf (Reference)
    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.medication_administration import (
        MedicationAdministration,
    )

    # status (EventStatus)
    from spark_auto_mapper_fhir.value_sets.event_status import EventStatusCode

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.procedure_not_performed_reason_snomed_ct_ import (
        ProcedureNotPerformedReason_SNOMED_CT_Code,
    )

    # End Import for CodeableConcept for statusReason
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.procedure_category_codes_snomedct_ import (
        ProcedureCategoryCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for category
    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.procedure_codes_snomedct_ import (
        ProcedureCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for code
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # performedDateTime (dateTime)
    # performedPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # performedString (string)
    # performedAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # performedRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # recorder (Reference)
    # Imports for References for recorder
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # asserter (Reference)
    # Imports for References for asserter
    # performer (Procedure.Performer)
    from spark_auto_mapper_fhir.backbone_elements.procedure_performer import (
        ProcedurePerformer,
    )

    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.procedure_reason_codes import (
        ProcedureReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # bodySite (CodeableConcept)
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # outcome (CodeableConcept)
    # Import for CodeableConcept for outcome
    from spark_auto_mapper_fhir.value_sets.procedure_outcome_codes_snomedct_ import (
        ProcedureOutcomeCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for outcome
    # report (Reference)
    # Imports for References for report
    from spark_auto_mapper_fhir.resources.composition import Composition

    # complication (CodeableConcept)
    # Import for CodeableConcept for complication
    from spark_auto_mapper_fhir.value_sets.condition_or__problem_or__diagnosis_codes import (
        Condition_or_Problem_or_DiagnosisCodesCode,
    )

    # End Import for CodeableConcept for complication
    # complicationDetail (Reference)
    # Imports for References for complicationDetail
    # followUp (CodeableConcept)
    # Import for CodeableConcept for followUp
    from spark_auto_mapper_fhir.value_sets.procedure_follow_up_codes_snomedct_ import (
        ProcedureFollowUpCodes_SNOMEDCT_Code,
    )

    # End Import for CodeableConcept for followUp
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # focalDevice (Procedure.FocalDevice)
    from spark_auto_mapper_fhir.backbone_elements.procedure_focal_device import (
        ProcedureFocalDevice,
    )

    # usedReference (Reference)
    # Imports for References for usedReference
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.substance import Substance

    # usedCode (CodeableConcept)
    # Import for CodeableConcept for usedCode
    from spark_auto_mapper_fhir.value_sets.fhir_device_types import FHIRDeviceTypesCode

    # End Import for CodeableConcept for usedCode


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Procedure(FhirResourceBase):
    """
    Procedure
    procedure.xsd
        An action that is or was performed on or for a patient. This can be a physical
    intervention like an operation, or less invasive like long term services,
    counseling, or hypnotherapy.
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
        basedOn: Optional[FhirList[Reference[Union[CarePlan, ServiceRequest]]]] = None,
        partOf: Optional[
            FhirList[Reference[Union[Procedure, Observation, MedicationAdministration]]]
        ] = None,
        status: EventStatusCode,
        statusReason: Optional[
            CodeableConcept[ProcedureNotPerformedReason_SNOMED_CT_Code]
        ] = None,
        category: Optional[
            CodeableConcept[ProcedureCategoryCodes_SNOMEDCT_Code]
        ] = None,
        code: Optional[CodeableConcept[ProcedureCodes_SNOMEDCT_Code]] = None,
        subject: Reference[Union[Patient, Group]],
        encounter: Optional[Reference[Encounter]] = None,
        performedDateTime: Optional[FhirDateTime] = None,
        performedPeriod: Optional[Period] = None,
        performedString: Optional[FhirString] = None,
        performedAge: Optional[Age] = None,
        performedRange: Optional[Range] = None,
        recorder: Optional[
            Reference[Union[Patient, RelatedPerson, Practitioner, PractitionerRole]]
        ] = None,
        asserter: Optional[
            Reference[Union[Patient, RelatedPerson, Practitioner, PractitionerRole]]
        ] = None,
        performer: Optional[FhirList[ProcedurePerformer]] = None,
        location: Optional[Reference[Location]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[ProcedureReasonCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        Procedure,
                        DiagnosticReport,
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        bodySite: Optional[
            FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]]
        ] = None,
        outcome: Optional[CodeableConcept[ProcedureOutcomeCodes_SNOMEDCT_Code]] = None,
        report: Optional[
            FhirList[Reference[Union[DiagnosticReport, DocumentReference, Composition]]]
        ] = None,
        complication: Optional[
            FhirList[CodeableConcept[Condition_or_Problem_or_DiagnosisCodesCode]]
        ] = None,
        complicationDetail: Optional[FhirList[Reference[Condition]]] = None,
        followUp: Optional[
            FhirList[CodeableConcept[ProcedureFollowUpCodes_SNOMEDCT_Code]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        focalDevice: Optional[FhirList[ProcedureFocalDevice]] = None,
        usedReference: Optional[
            FhirList[Reference[Union[Device, Medication, Substance]]]
        ] = None,
        usedCode: Optional[FhirList[CodeableConcept[FHIRDeviceTypesCode]]] = None,
    ) -> None:
        """
            An action that is or was performed on or for a patient. This can be a physical
        intervention like an operation, or less invasive like long term services,
        counseling, or hypnotherapy.
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
            :param identifier: Business identifiers assigned to this procedure by the performer or other
        systems which remain constant as the resource is updated and is propagated
        from server to server.
            :param instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, order set or other
        definition that is adhered to in whole or in part by this Procedure.
            :param instantiatesUri: The URL pointing to an externally maintained protocol, guideline, order set or
        other definition that is adhered to in whole or in part by this Procedure.
            :param basedOn: A reference to a resource that contains details of the request for this
        procedure.
            :param partOf: A larger event of which this particular procedure is a component or step.
            :param status: A code specifying the state of the procedure. Generally, this will be the in-
        progress or completed state.
            :param statusReason: Captures the reason for the current state of the procedure.
            :param category: A code that classifies the procedure for searching, sorting and display
        purposes (e.g. "Surgical Procedure").
            :param code: The specific procedure that is performed. Use text if the exact nature of the
        procedure cannot be coded (e.g. "Laparoscopic Appendectomy").
            :param subject: The person, animal or group on which the procedure was performed.
            :param encounter: The Encounter during which this Procedure was created or performed or to which
        the creation of this record is tightly associated.
            :param performedDateTime: None
            :param performedPeriod: None
            :param performedString: None
            :param performedAge: None
            :param performedRange: None
            :param recorder: Individual who recorded the record and takes responsibility for its content.
            :param asserter: Individual who is making the procedure statement.
            :param performer: Limited to "real" people rather than equipment.
            :param location: The location where the procedure actually happened.  E.g. a newborn at home, a
        tracheostomy at a restaurant.
            :param reasonCode: The coded reason why the procedure was performed. This may be a coded entity
        of some type, or may simply be present as text.
            :param reasonReference: The justification of why the procedure was performed.
            :param bodySite: Detailed and structured anatomical location information. Multiple locations
        are allowed - e.g. multiple punch biopsies of a lesion.
            :param outcome: The outcome of the procedure - did it resolve the reasons for the procedure
        being performed?
            :param report: This could be a histology result, pathology report, surgical report, etc.
            :param complication: Any complications that occurred during the procedure, or in the immediate
        post-performance period. These are generally tracked separately from the
        notes, which will typically describe the procedure itself rather than any
        'post procedure' issues.
            :param complicationDetail: Any complications that occurred during the procedure, or in the immediate
        post-performance period.
            :param followUp: If the procedure required specific follow up - e.g. removal of sutures. The
        follow up may be represented as a simple note or could potentially be more
        complex, in which case the CarePlan resource can be used.
            :param note: Any other notes and comments about the procedure.
            :param focalDevice: A device that is implanted, removed or otherwise manipulated (calibration,
        battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a
        focal portion of the Procedure.
            :param usedReference: Identifies medications, devices and any other substance used as part of the
        procedure.
            :param usedCode: Identifies coded items that were used as part of the procedure.
        """
        super().__init__(
            resourceType="Procedure",
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
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            category=category,
            code=code,
            subject=subject,
            encounter=encounter,
            performedDateTime=performedDateTime,
            performedPeriod=performedPeriod,
            performedString=performedString,
            performedAge=performedAge,
            performedRange=performedRange,
            recorder=recorder,
            asserter=asserter,
            performer=performer,
            location=location,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            bodySite=bodySite,
            outcome=outcome,
            report=report,
            complication=complication,
            complicationDetail=complicationDetail,
            followUp=followUp,
            note=note,
            focalDevice=focalDevice,
            usedReference=usedReference,
            usedCode=usedCode,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ProcedureSchema.get_schema(include_extension=include_extension)
