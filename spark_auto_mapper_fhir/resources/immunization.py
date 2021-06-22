from __future__ import annotations
from typing import Optional, Union, List, Any, TYPE_CHECKING

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.immunization import ImmunizationSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.immunization_status_codes import ImmunizationStatusCodes
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.complex_types.immunization_status_reason import ImmunizationStatusReason
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for vaccineCode
    from spark_auto_mapper_fhir.complex_types.vaccine_code import VaccineCode
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for reportOrigin
    from spark_auto_mapper_fhir.complex_types.immunization_report_origin import ImmunizationReportOrigin
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.date import FhirDate
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for site
    from spark_auto_mapper_fhir.complex_types.immunization_site import ImmunizationSite
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for route
    from spark_auto_mapper_fhir.complex_types.immunization_route import ImmunizationRoute
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity
    from spark_auto_mapper_fhir.backbone_elements.immunization_performer import ImmunizationPerformer
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.complex_types.immunization_reason import ImmunizationReason
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.complex_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for subpotentReason
    from spark_auto_mapper_fhir.complex_types.subpotent_reason import SubpotentReason
    from spark_auto_mapper_fhir.backbone_elements.immunization_education import ImmunizationEducation
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for programEligibility
    from spark_auto_mapper_fhir.complex_types.program_eligibility import ProgramEligibility
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    # Import for CodeableConcept for fundingSource
    from spark_auto_mapper_fhir.complex_types.funding_source import FundingSource
    from spark_auto_mapper_fhir.backbone_elements.immunization_reaction import ImmunizationReaction
    from spark_auto_mapper_fhir.backbone_elements.immunization_protocol_applied import ImmunizationProtocolApplied


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Immunization(FhirResourceBase):
    """
    """
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier ]] = None,
        status: ImmunizationStatusCodes ,
        statusReason: Optional[CodeableConcept[ImmunizationStatusReason] ] = None,
        vaccineCode: CodeableConcept[VaccineCode] ,
        patient: Reference [Union[Patient]],
        encounter: Optional[Reference [Union[Encounter]]] = None,
        recorded: Optional[FhirDateTime ] = None,
        primarySource: Optional[FhirBoolean ] = None,
        reportOrigin: Optional[CodeableConcept[ImmunizationReportOrigin] ] = None,
        location: Optional[Reference [Union[Location]]] = None,
        manufacturer: Optional[Reference [Union[Organization]]] = None,
        lotNumber: Optional[FhirString ] = None,
        expirationDate: Optional[FhirDate ] = None,
        site: Optional[CodeableConcept[ImmunizationSite] ] = None,
        route: Optional[CodeableConcept[ImmunizationRoute] ] = None,
        doseQuantity: Optional[Quantity ] = None,
        performer: Optional[FhirList[ImmunizationPerformer ]] = None,
        note: Optional[FhirList[Annotation ]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[ImmunizationReason] ]] = None,
        reasonReference: Optional[FhirList[Reference [Union[Condition, Observation, DiagnosticReport]]]] = None,
        isSubpotent: Optional[FhirBoolean ] = None,
        subpotentReason: Optional[FhirList[CodeableConcept[SubpotentReason] ]] = None,
        education: Optional[FhirList[ImmunizationEducation ]] = None,
        programEligibility: Optional[FhirList[CodeableConcept[ProgramEligibility] ]] = None,
        fundingSource: Optional[CodeableConcept[FundingSource] ] = None,
        reaction: Optional[FhirList[ImmunizationReaction ]] = None,
        protocolApplied: Optional[FhirList[ImmunizationProtocolApplied ]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param identifier: A unique identifier assigned to this immunization record.
        :param status: Indicates the current status of the immunization event.
        :param statusReason: Indicates the reason the immunization event was not performed.
        :param vaccineCode: Vaccine that was administered or was to be administered.
        :param patient: The patient who either received or did not receive the immunization.
        :param encounter: The visit or admission or other contact between patient and health care
    provider the immunization was performed as part of.
        :param recorded: The date the occurrence of the immunization was first captured in the record -
    potentially significantly after the occurrence of the event.
        :param primarySource: An indication that the content of the record is based on information from the
    person who administered the vaccine. This reflects the context under which the
    data was originally recorded.
        :param reportOrigin: The source of the data when the report of the immunization event is not based
    on information from the person who administered the vaccine.
        :param location: The service delivery location where the vaccine administration occurred.
        :param manufacturer: Name of vaccine manufacturer.
        :param lotNumber: Lot number of the  vaccine product.
        :param expirationDate: Date vaccine batch expires.
        :param site: Body site where vaccine was administered.
        :param route: The path by which the vaccine product is taken into the body.
        :param doseQuantity: The quantity of vaccine product that was administered.
        :param performer: Indicates who performed the immunization event.
        :param note: Extra information about the immunization that is not conveyed by the other
    attributes.
        :param reasonCode: Reasons why the vaccine was administered.
        :param reasonReference: Condition, Observation or DiagnosticReport that supports why the immunization
    was administered.
        :param isSubpotent: Indication if a dose is considered to be subpotent. By default, a dose should
    be considered to be potent.
        :param subpotentReason: Reason why a dose is considered to be subpotent.
        :param education: Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
        :param programEligibility: Indicates a patient's eligibility for a funding program.
        :param fundingSource: Indicates the source of the vaccine actually administered. This may be
    different than the patient eligibility (e.g. the patient may be eligible for a
    publically purchased vaccine but due to inventory issues, vaccine purchased
    with private funds was actually administered).
        :param reaction: Categorical data indicating that an adverse event is associated in time to an
    immunization.
        :param protocolApplied: The protocol (set of recommendations) being followed by the provider who
    administered the dose.
        """
        super().__init__(
            resourceType="Immunization",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            statusReason=statusReason,
            vaccineCode=vaccineCode,
            patient=patient,
            encounter=encounter,
            recorded=recorded,
            primarySource=primarySource,
            reportOrigin=reportOrigin,
            location=location,
            manufacturer=manufacturer,
            lotNumber=lotNumber,
            expirationDate=expirationDate,
            site=site,
            route=route,
            doseQuantity=doseQuantity,
            performer=performer,
            note=note,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            isSubpotent=isSubpotent,
            subpotentReason=subpotentReason,
            education=education,
            programEligibility=programEligibility,
            fundingSource=fundingSource,
            reaction=reaction,
            protocolApplied=protocolApplied,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ImmunizationSchema.get_schema(include_extension=include_extension)
