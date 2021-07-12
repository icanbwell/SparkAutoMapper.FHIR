from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicationstatement import (
    MedicationStatementSchema,
)

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
    from spark_auto_mapper_fhir.extensions.extension import Extension

    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # basedOn (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # partOf (Reference)
    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.medication_administration import (
        MedicationAdministration,
    )
    from spark_auto_mapper_fhir.resources.medication_dispense import MedicationDispense
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.observation import Observation

    # status (Medication Status Codes)
    from spark_auto_mapper_fhir.value_sets.medication_status_codes import (
        MedicationStatusCodesCode,
    )

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.snomedct_drug_therapy_status_codes import (
        SNOMEDCTDrugTherapyStatusCodesCode,
    )

    # End Import for CodeableConcept for statusReason
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.medication_usage_category_codes import (
        MedicationUsageCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
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
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group

    # context (Reference)
    # Imports for References for context
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.resources.episode_of_care import EpisodeOfCare

    # effectiveDateTime (dateTime)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # dateAsserted (dateTime)
    # informationSource (Reference)
    # Imports for References for informationSource
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # derivedFrom (Reference)
    # Imports for References for derivedFrom
    from spark_auto_mapper_fhir.resources.resource import Resource

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.condition_or__problem_or__diagnosis_codes import (
        Condition_or_Problem_or_DiagnosisCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # dosage (Dosage)
    from spark_auto_mapper_fhir.backbone_elements.dosage import Dosage


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationStatement(FhirResourceBase):
    """
    MedicationStatement
    medicationstatement.xsd
        A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the medication
    now or has taken the medication in the past or will be taking the medication
    in the future.  The source of this information can be the patient, significant
    other (such as a family member or spouse), or a clinician.  A common scenario
    where this information is captured is during the history taking process during
    a patient visit or stay.   The medication information may come from sources
    such as the patient's memory, from a prescription bottle,  or from a list of
    medications the patient, clinician or other party maintains.

    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration information
    from the person who administered the medication.  A medication statement is
    often, if not always, less specific.  There is no required date/time when the
    medication was administered, in fact we only know that a source has reported
    the patient is taking this medication, where details such as time, quantity,
    or rate or even medication product may be incomplete or missing or less
    precise.  As stated earlier, the medication statement information may come
    from the patient's memory, from a prescription bottle or from a list of
    medications the patient, clinician or other party maintains.  Medication
    administration is more formal and is not missing detailed information.
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
        extension: Optional[FhirList[Extension]] = None,
        modifierExtension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[
            FhirList[Reference[Union[MedicationRequest, CarePlan, ServiceRequest]]]
        ] = None,
        partOf: Optional[
            FhirList[
                Reference[
                    Union[
                        MedicationAdministration,
                        MedicationDispense,
                        MedicationStatement,
                        Procedure,
                        Observation,
                    ]
                ]
            ]
        ] = None,
        status: MedicationStatusCodesCode,
        statusReason: Optional[
            FhirList[CodeableConcept[SNOMEDCTDrugTherapyStatusCodesCode]]
        ] = None,
        category: Optional[CodeableConcept[MedicationUsageCategoryCodesCode]] = None,
        medicationCodeableConcept: Optional[
            CodeableConcept[SNOMEDCTMedicationCodesCode]
        ] = None,
        medicationReference: Optional[Reference[Union[Medication]]] = None,
        subject: Reference[Union[Patient, Group]],
        context: Optional[Reference[Union[Encounter, EpisodeOfCare]]] = None,
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        dateAsserted: Optional[FhirDateTime] = None,
        informationSource: Optional[
            Reference[
                Union[
                    Patient, Practitioner, PractitionerRole, RelatedPerson, Organization
                ]
            ]
        ] = None,
        derivedFrom: Optional[FhirList[Reference[Union[Resource]]]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[Condition_or_Problem_or_DiagnosisCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[Reference[Union[Condition, Observation, DiagnosticReport]]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        dosage: Optional[FhirList[Dosage]] = None,
    ) -> None:
        """
            A record of a medication that is being consumed by a patient.   A
        MedicationStatement may indicate that the patient may be taking the medication
        now or has taken the medication in the past or will be taking the medication
        in the future.  The source of this information can be the patient, significant
        other (such as a family member or spouse), or a clinician.  A common scenario
        where this information is captured is during the history taking process during
        a patient visit or stay.   The medication information may come from sources
        such as the patient's memory, from a prescription bottle,  or from a list of
        medications the patient, clinician or other party maintains.

        The primary difference between a medication statement and a medication
        administration is that the medication administration has complete
        administration information and is based on actual administration information
        often, if not always, less specific.  There is no required date/time when the
        medication was administered, in fact we only know that a source has reported
        the patient is taking this medication, where details such as time, quantity,
        or rate or even medication product may be incomplete or missing or less
        precise.  As stated earlier, the medication statement information may come
        medications the patient, clinician or other party maintains.  Medication
        administration is more formal and is not missing detailed information.
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
            :param identifier: Identifiers associated with this Medication Statement that are defined by
        business processes and/or used to refer to it when a direct URL reference to
        the resource itself is not appropriate. They are business identifiers assigned
        to this resource by the performer or other systems and remain constant as the
        resource is updated and propagates from server to server.
            :param basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.
            :param partOf: A larger event of which this particular event is a component or step.
            :param status: A code representing the patient or other source's judgment about the state of
        the medication used that this statement is about.  Generally, this will be
        active or completed.
            :param statusReason: Captures the reason for the current state of the MedicationStatement.
            :param category: Indicates where the medication is expected to be consumed or administered.
            :param medicationCodeableConcept: None
            :param medicationReference: None
            :param subject: The person, animal or group who is/was taking the medication.
            :param context: The encounter or episode of care that establishes the context for this
        MedicationStatement.
            :param effectiveDateTime: None
            :param effectivePeriod: None
            :param dateAsserted: The date when the medication statement was asserted by the information source.
            :param informationSource: The person or organization that provided the information about the taking of
        this medication. Note: Use derivedFrom when a MedicationStatement is derived
        from other resources, e.g. Claim or MedicationRequest.
            :param derivedFrom: Allows linking the MedicationStatement to the underlying MedicationRequest, or
        to other information that supports or is used to derive the
        MedicationStatement.
            :param reasonCode: A reason for why the medication is being/was taken.
            :param reasonReference: Condition or observation that supports why the medication is being/was taken.
            :param note: Provides extra information about the medication statement that is not conveyed
        by the other attributes.
            :param dosage: Indicates how the medication is/was or should be taken by the patient.
        """
        super().__init__(
            resourceType="MedicationStatement",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            category=category,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            context=context,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            dateAsserted=dateAsserted,
            informationSource=informationSource,
            derivedFrom=derivedFrom,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
            dosage=dosage,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicationStatementSchema.get_schema(include_extension=include_extension)
