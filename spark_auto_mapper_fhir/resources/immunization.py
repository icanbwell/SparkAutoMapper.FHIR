from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.immunization import ImmunizationSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (ImmunizationStatusCodes)
    from spark_auto_mapper_fhir.value_sets.immunization_status_codes import (
        ImmunizationStatusCodesCode,
    )

    # statusReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for statusReason
    from spark_auto_mapper_fhir.value_sets.immunization_status_reason_codes import (
        ImmunizationStatusReasonCodesCode,
    )

    # End Import for CodeableConcept for statusReason
    # vaccineCode (CodeableConcept)
    # Import for CodeableConcept for vaccineCode
    from spark_auto_mapper_fhir.value_sets.vaccine_administered_value_set import (
        VaccineAdministeredValueSetCode,
    )

    # End Import for CodeableConcept for vaccineCode
    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # recorded (dateTime)
    # primarySource (boolean)
    # reportOrigin (CodeableConcept)
    # Import for CodeableConcept for reportOrigin
    from spark_auto_mapper_fhir.value_sets.immunization_origin_codes import (
        ImmunizationOriginCodesCode,
    )

    # End Import for CodeableConcept for reportOrigin
    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # manufacturer (Reference)
    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization

    # lotNumber (string)
    # expirationDate (date)
    # site (CodeableConcept)
    # Import for CodeableConcept for site
    from spark_auto_mapper_fhir.value_sets.codes_for_immunization_site_of_administration import (
        CodesForImmunizationSiteOfAdministrationCode,
    )

    # End Import for CodeableConcept for site
    # route (CodeableConcept)
    # Import for CodeableConcept for route
    from spark_auto_mapper_fhir.value_sets.immunization_route_codes import (
        ImmunizationRouteCodesCode,
    )

    # End Import for CodeableConcept for route
    # doseQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # performer (Immunization.Performer)
    from spark_auto_mapper_fhir.backbone_elements.immunization_performer import (
        ImmunizationPerformer,
    )

    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.immunization_reason_codes import (
        ImmunizationReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport

    # isSubpotent (boolean)
    # subpotentReason (CodeableConcept)
    # Import for CodeableConcept for subpotentReason
    from spark_auto_mapper_fhir.value_sets.immunization_subpotent_reason import (
        ImmunizationSubpotentReasonCode,
    )

    # End Import for CodeableConcept for subpotentReason
    # education (Immunization.Education)
    from spark_auto_mapper_fhir.backbone_elements.immunization_education import (
        ImmunizationEducation,
    )

    # programEligibility (CodeableConcept)
    # Import for CodeableConcept for programEligibility
    from spark_auto_mapper_fhir.value_sets.immunization_program_eligibility import (
        ImmunizationProgramEligibilityCode,
    )

    # End Import for CodeableConcept for programEligibility
    # fundingSource (CodeableConcept)
    # Import for CodeableConcept for fundingSource
    from spark_auto_mapper_fhir.value_sets.immunization_funding_source import (
        ImmunizationFundingSourceCode,
    )

    # End Import for CodeableConcept for fundingSource
    # reaction (Immunization.Reaction)
    from spark_auto_mapper_fhir.backbone_elements.immunization_reaction import (
        ImmunizationReaction,
    )

    # protocolApplied (Immunization.ProtocolApplied)
    from spark_auto_mapper_fhir.backbone_elements.immunization_protocol_applied import (
        ImmunizationProtocolApplied,
    )

    # occurrenceDateTime (dateTime)
    # occurrenceString (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Immunization(FhirResourceBase):
    """
    Immunization
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ImmunizationStatusCodesCode,
        statusReason: Optional[
            CodeableConcept[ImmunizationStatusReasonCodesCode]
        ] = None,
        vaccineCode: CodeableConcept[VaccineAdministeredValueSetCode],
        patient: Reference[Union[Patient]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        recorded: Optional[FhirDateTime] = None,
        primarySource: Optional[FhirBoolean] = None,
        reportOrigin: Optional[CodeableConcept[ImmunizationOriginCodesCode]] = None,
        location: Optional[Reference[Union[Location]]] = None,
        manufacturer: Optional[Reference[Union[Organization]]] = None,
        lotNumber: Optional[FhirString] = None,
        expirationDate: Optional[FhirDate] = None,
        site: Optional[
            CodeableConcept[CodesForImmunizationSiteOfAdministrationCode]
        ] = None,
        route: Optional[CodeableConcept[ImmunizationRouteCodesCode]] = None,
        doseQuantity: Optional[Quantity] = None,
        performer: Optional[FhirList[ImmunizationPerformer]] = None,
        note: Optional[FhirList[Annotation]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[ImmunizationReasonCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[Reference[Union[Condition, Observation, DiagnosticReport]]]
        ] = None,
        isSubpotent: Optional[FhirBoolean] = None,
        subpotentReason: Optional[
            FhirList[CodeableConcept[ImmunizationSubpotentReasonCode]]
        ] = None,
        education: Optional[FhirList[ImmunizationEducation]] = None,
        programEligibility: Optional[
            FhirList[CodeableConcept[ImmunizationProgramEligibilityCode]]
        ] = None,
        fundingSource: Optional[CodeableConcept[ImmunizationFundingSourceCode]] = None,
        reaction: Optional[FhirList[ImmunizationReaction]] = None,
        protocolApplied: Optional[FhirList[ImmunizationProtocolApplied]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrenceString: Optional[FhirString] = None,
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
            :param occurrenceDateTime: None
            :param occurrenceString: None
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
            occurrenceDateTime=occurrenceDateTime,
            occurrenceString=occurrenceString,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ImmunizationSchema.get_schema(include_extension=include_extension)
