from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.observation import ObservationSchema

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
    from spark_auto_mapper_fhir.resources.care_plan import CarePlan
    from spark_auto_mapper_fhir.resources.device_request import DeviceRequest
    from spark_auto_mapper_fhir.resources.immunization_recommendation import (
        ImmunizationRecommendation,
    )
    from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
    from spark_auto_mapper_fhir.resources.nutrition_order import NutritionOrder
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # partOf (Reference)
    # Imports for References for partOf
    from spark_auto_mapper_fhir.resources.medication_administration import (
        MedicationAdministration,
    )
    from spark_auto_mapper_fhir.resources.medication_dispense import MedicationDispense
    from spark_auto_mapper_fhir.resources.medication_statement import (
        MedicationStatement,
    )
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.immunization import Immunization
    from spark_auto_mapper_fhir.resources.imaging_study import ImagingStudy

    # status (ObservationStatus)
    from spark_auto_mapper_fhir.value_sets.observation_status import (
        ObservationStatusCode,
    )

    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.observation_category_codes import (
        ObservationCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
    # code (CodeableConcept)
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.loinc_codes import LOINCCodesCode

    # End Import for CodeableConcept for code
    # subject (Reference)
    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.location import Location

    # focus (Reference)
    # Imports for References for focus
    from spark_auto_mapper_fhir.resources.resource import Resource

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # effectiveDateTime (dateTime)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # effectiveTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # effectiveInstant (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # issued (instant)
    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # valueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # valueCodeableConcept (CodeableConcept)
    # Import for CodeableConcept for valueCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for valueCodeableConcept
    # valueString (string)
    # valueBoolean (boolean)
    # valueInteger (integer)
    # valueRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # valueRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # valueSampledData (SampledData)
    from spark_auto_mapper_fhir.complex_types.sampled_data import SampledData

    # valueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # valueDateTime (dateTime)
    # valuePeriod (Period)
    # dataAbsentReason (CodeableConcept)
    # Import for CodeableConcept for dataAbsentReason
    from spark_auto_mapper_fhir.value_sets.data_absent_reason import (
        DataAbsentReasonCode,
    )

    # End Import for CodeableConcept for dataAbsentReason
    # interpretation (CodeableConcept)
    # Import for CodeableConcept for interpretation
    from spark_auto_mapper_fhir.value_sets.observation_interpretation_codes import (
        ObservationInterpretationCodesCode,
    )

    # End Import for CodeableConcept for interpretation
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # bodySite (CodeableConcept)
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # method (CodeableConcept)
    # Import for CodeableConcept for method
    from spark_auto_mapper_fhir.value_sets.observation_methods import (
        ObservationMethodsCode,
    )

    # End Import for CodeableConcept for method
    # specimen (Reference)
    # Imports for References for specimen
    from spark_auto_mapper_fhir.resources.specimen import Specimen

    # device (Reference)
    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device_metric import DeviceMetric

    # referenceRange (Observation.ReferenceRange)
    from spark_auto_mapper_fhir.backbone_elements.observation_reference_range import (
        ObservationReferenceRange,
    )

    # hasMember (Reference)
    # Imports for References for hasMember
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )
    from spark_auto_mapper_fhir.resources.molecular_sequence import MolecularSequence

    # derivedFrom (Reference)
    # Imports for References for derivedFrom
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.media import Media

    # component (Observation.Component)
    from spark_auto_mapper_fhir.backbone_elements.observation_component import (
        ObservationComponent,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Observation(FhirResourceBase):
    """
    Observation
    observation.xsd
        Measurements and simple assertions made about a patient, device or other
    subject.
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
            FhirList[
                Reference[
                    Union[
                        CarePlan,
                        DeviceRequest,
                        ImmunizationRecommendation,
                        MedicationRequest,
                        NutritionOrder,
                        ServiceRequest,
                    ]
                ]
            ]
        ] = None,
        partOf: Optional[
            FhirList[
                Reference[
                    Union[
                        MedicationAdministration,
                        MedicationDispense,
                        MedicationStatement,
                        Procedure,
                        Immunization,
                        ImagingStudy,
                    ]
                ]
            ]
        ] = None,
        status: ObservationStatusCode,
        category: Optional[
            FhirList[CodeableConcept[ObservationCategoryCodesCode]]
        ] = None,
        code: CodeableConcept[LOINCCodesCode],
        subject: Optional[Reference[Union[Patient, Group, Device, Location]]] = None,
        focus: Optional[FhirList[Reference[Union[Resource]]]] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        effectiveTiming: Optional[Timing] = None,
        effectiveInstant: Optional[FhirInstant] = None,
        issued: Optional[FhirInstant] = None,
        performer: Optional[
            FhirList[
                Reference[
                    Union[
                        Practitioner,
                        PractitionerRole,
                        Organization,
                        CareTeam,
                        Patient,
                        RelatedPerson,
                    ]
                ]
            ]
        ] = None,
        valueQuantity: Optional[Quantity] = None,
        valueCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        valueString: Optional[FhirString] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueRange: Optional[Range] = None,
        valueRatio: Optional[Ratio] = None,
        valueSampledData: Optional[SampledData] = None,
        valueTime: Optional[FhirTime] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        dataAbsentReason: Optional[CodeableConcept[DataAbsentReasonCode]] = None,
        interpretation: Optional[
            FhirList[CodeableConcept[ObservationInterpretationCodesCode]]
        ] = None,
        note: Optional[FhirList[Annotation]] = None,
        bodySite: Optional[CodeableConcept[SNOMEDCTBodyStructuresCode]] = None,
        method: Optional[CodeableConcept[ObservationMethodsCode]] = None,
        specimen: Optional[Reference[Union[Specimen]]] = None,
        device: Optional[Reference[Union[Device, DeviceMetric]]] = None,
        referenceRange: Optional[FhirList[ObservationReferenceRange]] = None,
        hasMember: Optional[
            FhirList[
                Reference[Union[Observation, QuestionnaireResponse, MolecularSequence]]
            ]
        ] = None,
        derivedFrom: Optional[
            FhirList[
                Reference[
                    Union[
                        DocumentReference,
                        ImagingStudy,
                        Media,
                        QuestionnaireResponse,
                        Observation,
                        MolecularSequence,
                    ]
                ]
            ]
        ] = None,
        component: Optional[FhirList[ObservationComponent]] = None,
    ) -> None:
        """
            Measurements and simple assertions made about a patient, device or other
        subject.
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
            :param identifier: A unique identifier assigned to this observation.
            :param basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.
        For example, a MedicationRequest may require a patient to have laboratory test
        performed before  it is dispensed.
            :param partOf: A larger event of which this particular Observation is a component or step.
        For example,  an observation as part of a procedure.
            :param status: The status of the result value.
            :param category: A code that classifies the general type of observation being made.
            :param code: Describes what was observed. Sometimes this is called the observation "name".
            :param subject: The patient, or group of patients, location, or device this observation is
        about and into whose record the observation is placed. If the actual focus of
        the observation is different from the subject (or a sample of, part, or region
        of the subject), the `focus` element or the `code` itself specifies the actual
        focus of the observation.
            :param focus: The actual focus of an observation when it is not the patient of record
        representing something or someone associated with the patient such as a
        spouse, parent, fetus, or donor. For example, fetus observations in a mother's
        record.  The focus of an observation could also be an existing condition,  an
        intervention, the subject's diet,  another observation of the subject,  or a
        body structure such as tumor or implanted device.   An example use case would
        be using the Observation resource to capture whether the mother is trained to
        change her child's tracheostomy tube. In this example, the child is the
        patient of record and the mother is the focus.
            :param encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
        during which this observation is made.
            :param effectiveDateTime: None
            :param effectivePeriod: None
            :param effectiveTiming: None
            :param effectiveInstant: None
            :param issued: The date and time this version of the observation was made available to
        providers, typically after the results have been reviewed and verified.
            :param performer: Who was responsible for asserting the observed value as "true".
            :param valueQuantity: None
            :param valueCodeableConcept: None
            :param valueString: None
            :param valueBoolean: None
            :param valueInteger: None
            :param valueRange: None
            :param valueRatio: None
            :param valueSampledData: None
            :param valueTime: None
            :param valueDateTime: None
            :param valuePeriod: None
            :param dataAbsentReason: Provides a reason why the expected value in the element Observation.value[x]
        is missing.
            :param interpretation: A categorical assessment of an observation value.  For example, high, low,
        normal.
            :param note: Comments about the observation or the results.
            :param bodySite: Indicates the site on the subject's body where the observation was made (i.e.
        the target site).
            :param method: Indicates the mechanism used to perform the observation.
            :param specimen: The specimen that was used when this observation was made.
            :param device: The device used to generate the observation data.
            :param referenceRange: Guidance on how to interpret the value by comparison to a normal or
        recommended range.  Multiple reference ranges are interpreted as an "OR".   In
        other words, to represent two distinct target populations, two
        `referenceRange` elements would be used.
            :param hasMember: This observation is a group observation (e.g. a battery, a panel of tests, a
        set of vital sign measurements) that includes the target as a member of the
        group.
            :param derivedFrom: The target resource that represents a measurement from which this observation
        value is derived. For example, a calculated anion gap or a fetal measurement
        based on an ultrasound image.
            :param component: Some observations have multiple component observations.  These component
        observations are expressed as separate code value pairs that share the same
        attributes.  Examples include systolic and diastolic component observations
        for blood pressure measurement and multiple component observations for
        genetics observations.
        """
        super().__init__(
            resourceType="Observation",
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
            category=category,
            code=code,
            subject=subject,
            focus=focus,
            encounter=encounter,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            effectiveTiming=effectiveTiming,
            effectiveInstant=effectiveInstant,
            issued=issued,
            performer=performer,
            valueQuantity=valueQuantity,
            valueCodeableConcept=valueCodeableConcept,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valueRange=valueRange,
            valueRatio=valueRatio,
            valueSampledData=valueSampledData,
            valueTime=valueTime,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            dataAbsentReason=dataAbsentReason,
            interpretation=interpretation,
            note=note,
            bodySite=bodySite,
            method=method,
            specimen=specimen,
            device=device,
            referenceRange=referenceRange,
            hasMember=hasMember,
            derivedFrom=derivedFrom,
            component=component,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ObservationSchema.get_schema(include_extension=include_extension)
