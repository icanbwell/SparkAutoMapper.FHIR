from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.riskassessment import RiskAssessmentSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for parent
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.complex_types.observation_status import (
        ObservationStatus,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for method
    from spark_auto_mapper_fhir.complex_types.risk_assessment_method import (
        RiskAssessmentMethod,
    )
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for condition
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for performer
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basis
    from spark_auto_mapper_fhir.resources.resource import Resource
    from spark_auto_mapper_fhir.backbone_elements.risk_assessment_prediction import (
        RiskAssessmentPrediction,
    )
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RiskAssessment(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[Reference[Union[Resource]]] = None,
        parent: Optional[Reference[Union[Resource]]] = None,
        status: ObservationStatus,
        method: Optional[CodeableConcept[RiskAssessmentMethod]] = None,
        code: Optional[CodeableConcept] = None,
        subject: Reference[Union[Patient, Group]],
        encounter: Optional[Reference[Union[Encounter]]] = None,
        condition: Optional[Reference[Union[Condition]]] = None,
        performer: Optional[
            Reference[Union[Practitioner, PractitionerRole, Device]]
        ] = None,
        reasonCode: Optional[FhirList[CodeableConcept]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Observation, DiagnosticReport, DocumentReference]
                ]
            ]
        ] = None,
        basis: Optional[FhirList[Reference[Union[Resource]]]] = None,
        prediction: Optional[FhirList[RiskAssessmentPrediction]] = None,
        mitigation: Optional[FhirString] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifier assigned to the risk assessment.
            :param basedOn: A reference to the request that is fulfilled by this risk assessment.
            :param parent: A reference to a resource that this risk assessment is part of, such as a
        Procedure.
            :param status: The status of the RiskAssessment, using the same statuses as an Observation.
            :param method: The algorithm, process or mechanism used to evaluate the risk.
            :param code: The type of the risk assessment performed.
            :param subject: The patient or group the risk assessment applies to.
            :param encounter: The encounter where the assessment was performed.
            :param condition: For assessments or prognosis specific to a particular condition, indicates the
        condition being assessed.
            :param performer: The provider or software application that performed the assessment.
            :param reasonCode: The reason the risk assessment was performed.
            :param reasonReference: Resources supporting the reason the risk assessment was performed.
            :param basis: Indicates the source data considered as part of the assessment (for example,
        FamilyHistory, Observations, Procedures, Conditions, etc.).
            :param prediction: Describes the expected outcome for the subject.
            :param mitigation: A description of the steps that might be taken to reduce the identified
        risk(s).
            :param note: Additional comments about the risk assessment.
        """
        super().__init__(
            resourceType="RiskAssessment",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            basedOn=basedOn,
            parent=parent,
            status=status,
            method=method,
            code=code,
            subject=subject,
            encounter=encounter,
            condition=condition,
            performer=performer,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            basis=basis,
            prediction=prediction,
            mitigation=mitigation,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return RiskAssessmentSchema.get_schema(include_extension=include_extension)