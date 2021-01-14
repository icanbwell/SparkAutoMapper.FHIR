from typing import Optional, Union
from pyspark.sql.types import StructType
from spark_auto_mapper_fhir.complex_types.attachment import Attachment

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.backbone_elements.diagnostic_report_media_backbone_element import \
    DiagnosticReportMediaBackboneElement
from spark_auto_mapper_fhir.resources.imaging_study import ImagingStudy
from spark_auto_mapper_fhir.resources.nutrition_order import NutritionOrder
from spark_auto_mapper_fhir.resources.observation import Observation

from spark_auto_mapper_fhir.resources.care_team import CareTeam

from spark_auto_mapper_fhir.resources.organization import Organization

from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

from spark_auto_mapper_fhir.resources.practitioner import Practitioner

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

from spark_auto_mapper_fhir.resources.encounter import Encounter

from spark_auto_mapper_fhir.resources.location import Location

from spark_auto_mapper_fhir.resources.device import Device

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.resources.patient import Patient

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

from spark_auto_mapper_fhir.resources.medication_request import MedicationRequest

from spark_auto_mapper_fhir.resources.immunization_recommendation import ImmunizationRecommendation

from spark_auto_mapper_fhir.resources.care_plan import CarePlan

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.resources.diagnosticreport import DiagnosticReportSchema

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.resources.specimen import Specimen
from spark_auto_mapper_fhir.valuesets.diagnostic_report_status import DiagnosticReportStatusCode
from spark_auto_mapper_fhir.valuesets.diagnostic_service_sections import DiagnosticServiceSectionCode
from spark_auto_mapper_fhir.valuesets.report_codes import LOINCDiagnosticReportCode
from spark_auto_mapper_fhir.valuesets.snomed_clinical_finding import SNOMEDCTClinicalFindingsCode


class DiagnosticReport(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        status: DiagnosticReportStatusCode,
        code: LOINCDiagnosticReportCode,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[FhirList[Reference[Union[CarePlan,
                                                   ImmunizationRecommendation,
                                                   MedicationRequest,
                                                   NutritionOrder,
                                                   ServiceRequest]]]] = None,
        category: Optional[FhirList[
            CodeableConcept[DiagnosticServiceSectionCode]]] = None,
        subject: Optional[Reference[Union[Patient, Group, Device,
                                          Location]]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        effectiveDateTime: Optional[FhirDateTime] = None,
        effectivePeriod: Optional[Period] = None,
        issued: Optional[FhirInstant] = None,
        performer: Optional[FhirList[Reference[Union[Practitioner,
                                                     PractitionerRole,
                                                     Organization,
                                                     CareTeam]]]] = None,
        resultsInterpreter: Optional[FhirList[Reference[Union[Practitioner,
                                                              PractitionerRole,
                                                              Organization,
                                                              CareTeam]]]
                                     ] = None,
        specimen: Optional[Reference[Specimen]] = None,
        result: Optional[FhirList[Reference[Observation]]] = None,
        imagingStudy: Optional[FhirList[Reference[ImagingStudy]]] = None,
        media: Optional[FhirList[DiagnosticReportMediaBackboneElement]] = None,
        conclusion: Optional[FhirString] = None,
        conclusionCode: Optional[FhirList[
            CodeableConcept[SNOMEDCTClinicalFindingsCode]]] = None,
        presentedForm: Optional[FhirList[Attachment]] = None
    ) -> None:
        """
        DiagnosticReport Resource in FHIR
        https://www.hl7.org/fhir/diagnosticreport.html
        A Diagnostic report - a combination of request information, atomic results, images, interpretation,
        as well as formatted reports


        :param id_: id of resource
        :param identifier: Business identifier for report
        :param basedOn: What was requested
        :param status: registered | partial | preliminary | final +
        :param category: Service category
        :param code: Name/Code for this diagnostic report
        :param subject: The subject of the report - usually, but not always, the patient
        :param encounter: Health care event when test ordered
        :param effectiveDateTime: Clinically relevant time/time-period for report
        :param effectivePeriod: Clinically relevant time/time-period for report
        :param issued: DateTime this version was made
        :param performer: Responsible Diagnostic Service
        :param resultsInterpreter:  PractitionerRole | Organization | CareTeam)	Primary result interpreter
        :param specimen: Specimens this report is based on
        :param result: Observations
        :param imagingStudy: Reference to full details of imaging associated with the diagnostic report
        :param media: Key images associated with this report
        :param conclusion: Clinical conclusion (interpretation) of test results
        :param conclusionCode: Codes for the clinical conclusion of test results
        :param presentedForm: Entire report as issued
        """
        super().__init__(
            resourceType="DiagnosticReport",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            basedOn=basedOn,
            status=status,
            category=category,
            code=code,
            subject=subject,
            encounter=encounter,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            issued=issued,
            performer=performer,
            resultsInterpreter=resultsInterpreter,
            specimen=specimen,
            result=result,
            imagingStudy=imagingStudy,
            media=media,
            conclusion=conclusion,
            conclusionCode=conclusionCode,
            presentedForm=presentedForm
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return DiagnosticReportSchema.get_schema(
            include_extension=include_extension
        )
