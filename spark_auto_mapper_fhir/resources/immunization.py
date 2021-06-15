from __future__ import annotations
from typing import Optional, Union, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

if TYPE_CHECKING:
    from spark_fhir_schemas.r4.resources.immunization import ImmunizationSchema

    from spark_auto_mapper_fhir.backbone_elements.Immunization_reaction_backbone_element import (
        ImmunizationReactionBackboneElement,
    )
    from spark_auto_mapper_fhir.backbone_elements.immunization_education_backbone_element import (
        ImmunizationEducationBackboneElement,
    )
    from spark_auto_mapper_fhir.backbone_elements.immunization_performer_backbone_element import (
        ImmunizationPerformerBackboneElement,
    )
    from spark_auto_mapper_fhir.backbone_elements.immunization_protocolApplied_backbone_element import (
        ImmunizationProtocolAppliedBackboneElement,
    )
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation
    from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference
    from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity
    from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
    from spark_auto_mapper_fhir.fhir_types.date import FhirDate
    from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.fhir_types.id import FhirId
    from spark_auto_mapper_fhir.fhir_types.list import FhirList
    from spark_auto_mapper_fhir.fhir_types.string import FhirString
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.extensions.extension import Extension
    from spark_auto_mapper_fhir.complex_types.meta import Meta
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.valuesets.immunization_funding_source import (
        ImmunizationFundingSourceCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_origin import (
        ImmunizationOriginCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_program_elegibility import (
        ImmunizationProgramElegibilityCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_reason_code import (
        ImmunizationReasonCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_route import (
        ImmunizationRouteCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_site import ImmunizationSiteCode
    from spark_auto_mapper_fhir.valuesets.immunization_status import (
        ImmunizationStatusCode,
    )
    from spark_auto_mapper_fhir.valuesets.immunization_status_reason import (
        ImmunizationStatusReasonCode,
    )
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.valuesets.immunization_subpotent_reason import (
        ImmunizationSubpotentReasonCode,
    )
    from spark_auto_mapper_fhir.valuesets.vaccine_code import VaccineCode


class Immunization(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ImmunizationStatusCode,
        statusReason: Optional[CodeableConcept[ImmunizationStatusReasonCode]] = None,
        vaccineCode: CodeableConcept[VaccineCode],
        patient: Reference[Patient],
        encounter: Optional[Reference[Encounter]] = None,
        occurrenceDateTime: Optional[FhirDateTime] = None,
        occurrenceString: Optional[FhirString] = None,
        recorded: Optional[FhirDateTime] = None,
        primarySource: Optional[FhirBoolean] = None,
        reportOrigin: Optional[CodeableConcept[ImmunizationOriginCode]] = None,
        location: Optional[Reference[Location]] = None,
        manufacturer: Optional[Reference[Organization]] = None,
        lotNumber: Optional[FhirString] = None,
        expirationDate: Optional[FhirDate] = None,
        site: Optional[CodeableConcept[ImmunizationSiteCode]] = None,
        route: Optional[CodeableConcept[ImmunizationRouteCode]] = None,
        doseQuantity: Optional[SimpleQuantity] = None,
        performer: Optional[FhirList[ImmunizationPerformerBackboneElement]] = None,
        note: Optional[FhirList[Annotation]] = None,
        reasonCode: Optional[FhirList[CodeableConcept[ImmunizationReasonCode]]] = None,
        reasonReference: Optional[
            FhirList[Reference[Union[Condition, Observation, "DiagnosticReport"]]]
        ] = None,
        isSubpotent: Optional[FhirBoolean] = None,
        subpotentReason: Optional[
            CodeableConcept[ImmunizationSubpotentReasonCode]
        ] = None,
        education: Optional[FhirList[ImmunizationEducationBackboneElement]] = None,
        programEligibility: Optional[
            FhirList[CodeableConcept[ImmunizationProgramElegibilityCode]]
        ] = None,
        fundingSource: Optional[CodeableConcept[ImmunizationFundingSourceCode]] = None,
        reaction: Optional[FhirList[ImmunizationReactionBackboneElement]] = None,
        protocolApplied: Optional[ImmunizationProtocolAppliedBackboneElement] = None,
    ) -> None:
        """
        Immunization Resource in FHIR
        https://www.hl7.org/fhir/immunization.html
        TODO: Fill this

        :param id_: id of resource
        :param status: completed | entered-in-error | not-done
        :param statusReason: Reason not done
        :param vaccineCode: Vaccine product administered
        :param patient: Who was immunized
        :param encounter: Encounter immunization was part of
        :param recorded: When the immunization was first captured in the subject's record
        :param primarySource: Indicates context the data was recorded in
        :param reportOrigin: Indicates the source of a secondarily reported record
        :param location: Where immunization occurred
        :param manufacturer: Vaccine manufacturer
        :param lotNumber: Vaccine lot number
        :param expirationDate: Vaccine expiration date
        :param site: Body site vaccine was administered
        :param route: How vaccine entered body
        :param doseQuantity: Amount of vaccine administered
        :param performer: Who performed event
        :param note: Who performed event
        :param reasonCode: Why immunization occurred
        :param reasonReference: Why immunization occurred
        :param subpotentReason: Reason for being subpotent
        :param education: Educational material presented to patient
        :param programEligibility: Patient eligibility for a vaccination program
        :param fundingSource: Funding source for the vaccine
        :param reaction: Details of a reaction that follows immunization
        :param protocolApplied: Protocol followed by the provider


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
