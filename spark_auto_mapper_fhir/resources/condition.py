from typing import Optional, Union

from pyspark.sql.types import StructType
from spark_auto_mapper_fhir.complex_types.annotation import Annotation

from spark_auto_mapper_fhir.backbone_elements.condition_evidence_backbone_element import \
    ConditionEvidenceBackboneElement
from spark_auto_mapper_fhir.backbone_elements.condition_stage_backbone_element import ConditionStageBackboneElement
from spark_auto_mapper_fhir.resources.practitioner import Practitioner

from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.fhir_types.age import FhirAge
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.resources.encounter import Encounter

from spark_auto_mapper_fhir.resources.patient import Patient

from spark_auto_mapper_fhir.resources.group import Group
from spark_fhir_schemas.r4.resources.condition import ConditionSchema

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.valuesets.body_site import SNOMEDCTBodyStructuresCode
from spark_auto_mapper_fhir.valuesets.condition import ConditionCode
from spark_auto_mapper_fhir.valuesets.condition_category import ConditionCategoryCode
from spark_auto_mapper_fhir.valuesets.condition_clinical import ConditionClinicalStatusCode
from spark_auto_mapper_fhir.valuesets.condition_severity import ConditionSeverityCode
from spark_auto_mapper_fhir.valuesets.condition_verification_status import ConditionVerificationStatusCode


class Condition(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        subject: Reference[Union[Patient, Group]],
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        clinicalStatus: Optional[CodeableConcept[ConditionClinicalStatusCode]
                                 ] = None,
        verificationStatus: Optional[
            CodeableConcept[ConditionVerificationStatusCode]] = None,
        category: Optional[FhirList[CodeableConcept[ConditionCategoryCode]]
                           ] = None,
        severity: Optional[CodeableConcept[ConditionSeverityCode]] = None,
        code: Optional[CodeableConcept[ConditionCode]] = None,
        bodySite: Optional[FhirList[CodeableConcept[SNOMEDCTBodyStructuresCode]
                                    ]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        onsetDateTime: Optional[FhirDateTime] = None,
        onsetAge: Optional[FhirAge] = None,
        onsetPeriod: Optional[Period] = None,
        onsetRange: Optional[Range] = None,
        onsetString: Optional[FhirString] = None,
        abatementDateTime: Optional[FhirDateTime] = None,
        abatementAge: Optional[FhirAge] = None,
        abatementPeriod: Optional[Period] = None,
        abatementRange: Optional[Range] = None,
        abatementString: Optional[FhirString] = None,
        recordedDate: Optional[FhirDateTime] = None,
        recorder: Optional[Reference[Union[Practitioner, PractitionerRole,
                                           Patient, RelatedPerson]]] = None,
        asserter: Optional[Reference[Union[Practitioner, PractitionerRole,
                                           Patient, RelatedPerson]]] = None,
        stage: Optional[FhirList[ConditionStageBackboneElement]] = None,
        evidence: Optional[FhirList[ConditionEvidenceBackboneElement]] = None,
        note: Optional[FhirList[Annotation]] = None
    ) -> None:
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition
        Detailed information about conditions, problems or diagnoses
        + Guideline: Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item
        + Rule: If condition is abated, then clinicalStatus must be either inactive, resolved, or remission
        + Rule: Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error

        :param id_: id of resource
        :param identifier: External Ids for this condition
        :param clinicalStatus: active | recurrence | relapse | inactive | remission | resolved
        :param verificationStatus: unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
        :param category: problem-list-item | encounter-diagnosis
        :param severity: Subjective severity of condition
        :param code: Identification of the condition, problem or diagnosis
        :param bodySite: Anatomical location, if relevant
        :param subject: Who has the condition?
        :param encounter: Encounter created as part of
        :param onsetDateTime: Estimated or actual date, date-time, or age
        :param onsetAge: Estimated or actual date, date-time, or age
        :param onsetPeriod: Estimated or actual date, date-time, or age
        :param onsetRange: Estimated or actual date, date-time, or age
        :param onsetString: Estimated or actual date, date-time, or age
        :param abatementDateTime: When in resolution/remission
        :param abatementAge: When in resolution/remission
        :param abatementPeriod: When in resolution/remission
        :param abatementRange: When in resolution/remission
        :param abatementString: When in resolution/remission
        :param recordedDate: Date record was first recorded
        :param recorder: Who recorded the condition
        :param asserter: Person who asserts this condition
        :param stage: Stage/grade, usually assessed formally
                        + Rule: Stage SHALL have summary or assessment
        :param evidence: Supporting evidence
                        + Rule: evidence SHALL have code or details
        :param note: Additional information about the Condition
        """
        super().__init__(
            resourceType="Condition",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            clinicalStatus=clinicalStatus,
            verificationStatus=verificationStatus,
            category=category,
            severity=severity,
            code=code,
            bodySite=bodySite,
            subject=subject,
            encounter=encounter,
            onsetDateTime=onsetDateTime,
            onsetAge=onsetAge,
            onsetPeriod=onsetPeriod,
            onsetRange=onsetRange,
            onsetString=onsetString,
            abatementDateTime=abatementDateTime,
            abatementAge=abatementAge,
            abatementPeriod=abatementPeriod,
            abatementRange=abatementRange,
            abatementString=abatementString,
            recordedDate=recordedDate,
            recorder=recorder,
            asserter=asserter,
            stage=stage,
            evidence=evidence,
            note=note
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ConditionSchema.get_schema(include_extension=include_extension)
