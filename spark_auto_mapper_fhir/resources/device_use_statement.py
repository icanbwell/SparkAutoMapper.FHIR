from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.deviceusestatement import DeviceUseStatementSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.complex_types.device_use_statement_status import (
        DeviceUseStatementStatus,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for derivedFrom
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.claim import Claim
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.questionnaire_response import (
        QuestionnaireResponse,
    )
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.diagnostic_report import DiagnosticReport
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.media import Media
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.complex_types.body_site import BodySite
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceUseStatement(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        basedOn: Optional[FhirList[Reference[Union[ServiceRequest]]]] = None,
        status: DeviceUseStatementStatus,
        subject: Reference[Union[Patient, Group]],
        derivedFrom: Optional[
            FhirList[
                Reference[
                    Union[
                        ServiceRequest,
                        Procedure,
                        Claim,
                        Observation,
                        QuestionnaireResponse,
                        DocumentReference,
                    ]
                ]
            ]
        ] = None,
        recordedOn: Optional[FhirDateTime] = None,
        source: Optional[
            Reference[Union[Patient, Practitioner, PractitionerRole, RelatedPerson]]
        ] = None,
        device: Reference[Union[Device]],
        reasonCode: Optional[FhirList[CodeableConcept]] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[
                        Condition,
                        Observation,
                        DiagnosticReport,
                        DocumentReference,
                        Media,
                    ]
                ]
            ]
        ] = None,
        bodySite: Optional[CodeableConcept[BodySite]] = None,
        note: Optional[FhirList[Annotation]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: An external identifier for this statement such as an IRI.
            :param basedOn: A plan, proposal or order that is fulfilled in whole or in part by this
        DeviceUseStatement.
            :param status: A code representing the patient or other source's judgment about the state of
        the device used that this statement is about.  Generally this will be active
        or completed.
            :param subject: The patient who used the device.
            :param derivedFrom: Allows linking the DeviceUseStatement to the underlying Request, or to other
        information that supports or is used to derive the DeviceUseStatement.
            :param recordedOn: The time at which the statement was made/recorded.
            :param source: Who reported the device was being used by the patient.
            :param device: The details of the device used.
            :param reasonCode: Reason or justification for the use of the device.
            :param reasonReference: Indicates another resource whose existence justifies this DeviceUseStatement.
            :param bodySite: Indicates the anotomic location on the subject's body where the device was
        used ( i.e. the target).
            :param note: Details about the device statement that were not represented at all or
        sufficiently in one of the attributes provided in a class. These may include
        for example a comment, an instruction, or a note associated with the
        statement.
        """
        super().__init__(
            resourceType="DeviceUseStatement",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            basedOn=basedOn,
            status=status,
            subject=subject,
            derivedFrom=derivedFrom,
            recordedOn=recordedOn,
            source=source,
            device=device,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            bodySite=bodySite,
            note=note,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return DeviceUseStatementSchema.get_schema(include_extension=include_extension)