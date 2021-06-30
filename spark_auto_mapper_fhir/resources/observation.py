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
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.observation import ObservationSchema

if TYPE_CHECKING:
    pass
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

    # issued (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # performer (Reference)
    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.care_team import CareTeam
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

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

    # effectiveDateTime (dateTime)
    # effectivePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # effectiveTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # effectiveInstant (instant)
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


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Observation(FhirResourceBase):
    """
    Observation
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
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
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        effectiveTiming: Optional[Timing] = None,
        effectiveInstant: Optional[FhirInstant] = None,
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
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
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
            :param issued: The date and time this version of the observation was made available to
        providers, typically after the results have been reviewed and verified.
            :param performer: Who was responsible for asserting the observed value as "true".
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
            :param effectiveDateTime: None
            :param effectivePeriod: None
            :param effectiveTiming: None
            :param effectiveInstant: None
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
        """
        super().__init__(
            resourceType="Observation",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            category=category,
            code=code,
            subject=subject,
            focus=focus,
            encounter=encounter,
            issued=issued,
            performer=performer,
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
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            effectiveTiming=effectiveTiming,
            effectiveInstant=effectiveInstant,
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
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ObservationSchema.get_schema(include_extension=include_extension)
