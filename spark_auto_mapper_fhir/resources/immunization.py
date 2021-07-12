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
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.immunization import ImmunizationSchema

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

    # occurrenceDateTime (dateTime)
    # occurrenceString (string)
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


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Immunization(FhirResourceBase):
    """
    Immunization
    immunization.xsd
        Describes the event of a patient being administered a vaccine or a record of
    an immunization as reported by a patient, a clinician or another party.
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
        status: ImmunizationStatusCodesCode,
        statusReason: Optional[
            CodeableConcept[ImmunizationStatusReasonCodesCode]
        ] = None,
        vaccineCode: CodeableConcept[VaccineAdministeredValueSetCode],
        patient: Reference[Union[Patient]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrenceString: Optional[FhirString] = None,
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
    ) -> None:
        """
            Describes the event of a patient being administered a vaccine or a record of
        an immunization as reported by a patient, a clinician or another party.
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
            :param identifier: A unique identifier assigned to this immunization record.
            :param status: Indicates the current status of the immunization event.
            :param statusReason: Indicates the reason the immunization event was not performed.
            :param vaccineCode: Vaccine that was administered or was to be administered.
            :param patient: The patient who either received or did not receive the immunization.
            :param encounter: The visit or admission or other contact between patient and health care
        provider the immunization was performed as part of.
            :param occurrenceDateTime: None
            :param occurrenceString: None
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
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            statusReason=statusReason,
            vaccineCode=vaccineCode,
            patient=patient,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrenceString=occurrenceString,
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
