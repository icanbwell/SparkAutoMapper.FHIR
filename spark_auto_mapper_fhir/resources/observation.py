from typing import Optional, Union, Any

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.observation import ObservationSchema

from spark_auto_mapper_fhir.backbone_elements.observation_component_backbone_element import \
    ObservationComponentBackboneElement
from spark_auto_mapper_fhir.backbone_elements.observation_reference_range_backbone_element import \
    ObservationReferenceRangeBackboneElement
from spark_auto_mapper_fhir.backbone_elements.timing_backbone_element import Timing
from spark_auto_mapper_fhir.complex_types.annotation import Annotation
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.quantity import Quantity
from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.complex_types.ratio import Ratio
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.complex_types.sampled_data import SampledData
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.time import FhirTime
from spark_auto_mapper_fhir.resources.care_plan import CarePlan
from spark_auto_mapper_fhir.resources.care_team import CareTeam
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.device_metric import DeviceMetric
from spark_auto_mapper_fhir.resources.device_request import DeviceRequest
from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.imaging_study import ImagingStudy
from spark_auto_mapper_fhir.resources.immunization import Immunization
from spark_auto_mapper_fhir.resources.immunization_recommendation import ImmunizationRecommendation
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.media import Media
from spark_auto_mapper_fhir.resources.medication_administration import MedicationAdministration
from spark_auto_mapper_fhir.resources.medication_dispense import MedicationDispense
from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest
from spark_auto_mapper_fhir.resources.medication_statement import MedicationStatement
from spark_auto_mapper_fhir.resources.molecular_sequence import MolecularSequence
from spark_auto_mapper_fhir.resources.nutrition_order import NutritionOrder
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.resources.questionnaire_response import QuestionnaireResponse
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
from spark_auto_mapper_fhir.resources.specimen import Specimen
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.body_site import SNOMEDCTBodyStructuresCode
from spark_auto_mapper_fhir.valuesets.data_absent_reason import DataAbsentReasonCode
from spark_auto_mapper_fhir.valuesets.observation_category import ObservationCategoryCode
from spark_auto_mapper_fhir.valuesets.observation_code import LOINCCode
from spark_auto_mapper_fhir.valuesets.observation_interpretation import ObservationInterpretationCode
from spark_auto_mapper_fhir.valuesets.observation_methods import ObservationMethodsCode
from spark_auto_mapper_fhir.valuesets.observation_status import ObservationStatusCode


class Observation(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        status: ObservationStatusCode,
        code: CodeableConcept[LOINCCode],
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[FhirList[Reference[Union[CarePlan, DeviceRequest,
                                                   ImmunizationRecommendation,
                                                   MedicationRequest,
                                                   NutritionOrder,
                                                   ServiceRequest]]]] = None,
        partOf: Optional[FhirList[Reference[Union[MedicationAdministration,
                                                  MedicationDispense,
                                                  MedicationStatement,
                                                  Procedure, Immunization,
                                                  ImagingStudy]]]] = None,
        category: Optional[FhirList[CodeableConcept[ObservationCategoryCode]]
                           ] = None,
        subject: Optional[Reference[Union[Patient, Group, Device,
                                          Location]]] = None,
        focus: Optional[FhirList[Any]] = None,
        encounter: Optional[Encounter] = None,
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        effectiveTiming: Optional[Timing] = None,
        effectiveInstant: Optional[FhirInstant] = None,
        issued: Optional[FhirInstant] = None,
        performer: Optional[FhirList[Reference[Union[Practitioner,
                                                     PractitionerRole,
                                                     Organization, CareTeam,
                                                     Patient,
                                                     RelatedPerson]]]] = None,
        valueQuantity: Optional[Quantity] = None,
        valueCodeableConcept: Optional[CodeableConcept[FhirValueSetBase]
                                       ] = None,
        valueString: Optional[FhirString] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueRange: Optional[Range] = None,
        valueRatio: Optional[Ratio] = None,
        valueSampledData: Optional[SampledData] = None,
        valueTime: Optional[FhirTime] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        dataAbsentReason: Optional[CodeableConcept[DataAbsentReasonCode]
                                   ] = None,
        interpretation: Optional[FhirList[ObservationInterpretationCode]
                                 ] = None,
        note: Optional[FhirList[Annotation]] = None,
        bodySite: Optional[CodeableConcept[SNOMEDCTBodyStructuresCode]] = None,
        method: Optional[CodeableConcept[ObservationMethodsCode]] = None,
        specimen: Optional[Reference[Specimen]] = None,
        device: Optional[Reference[Union[Device, DeviceMetric]]] = None,
        referenceRange: Optional[
            FhirList[ObservationReferenceRangeBackboneElement]] = None,
        hasMember: Optional[FhirList[Reference[Union['Observation',
                                                     QuestionnaireResponse,
                                                     MolecularSequence]]]
                            ] = None,
        derivedFrom: Optional[FhirList[Reference[Union[DocumentReference,
                                                       ImagingStudy, Media,
                                                       QuestionnaireResponse,
                                                       'Observation',
                                                       MolecularSequence]]]
                              ] = None,
        component: Optional[FhirList[ObservationComponentBackboneElement]
                            ] = None
    ) -> None:
        """
        Observation Resource in FHIR
        http://hl7.org/fhir/observation.html
        Measurements and simple assertions
        + Rule: dataAbsentReason SHALL only be present if Observation.value[x] is not present
        + Rule: If Observation.code is the same as an Observation.component.code then the value element associated
         with the code SHALL NOT be present


        :param id_: id of resource
        :param identifier: Business Identifier for observation
        :param basedOn: Fulfills plan, proposal or order
        :param partOf: Part of referenced event
        :param status: registered | preliminary | final | amended +
        :param category: Classification of type of observation
        :param code: Type of observation (code / type)
        :param subject: Who and/or what the observation is about
        :param focus: What the observation is about, when it is not about the subject of record
        :param encounter: Healthcare event during which this observation is made
        :param effectiveDateTime: Clinically relevant time/time-period for observation
        :param effectivePeriod: Clinically relevant time/time-period for observation
        :param effectiveTiming: Clinically relevant time/time-period for observation
        :param effectiveInstant: Clinically relevant time/time-period for observation
        :param issued: Date/Time this version was made available
        :param performer: Who is responsible for the observation
        :param dataAbsentReason: Why the result is missing
        :param interpretation: High, low, normal, etc.
        :param note: Comments about the observation
        :param bodySite: Observed body part
        :param method: How it was done
        :param specimen: Specimen used for this observation
        :param device: (Measurement) Device
        :param referenceRange: Provides guide for interpretation
                                + Rule: Must have at least a low or a high or text
        :param hasMember: Related resource that belongs to the Observation group
        :param derivedFrom: Related measurements the observation is made from
        :param component: 	Component results
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
            component=component
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ObservationSchema.get_schema(
            include_extension=include_extension
        )
