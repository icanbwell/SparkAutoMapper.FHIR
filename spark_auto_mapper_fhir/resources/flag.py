from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.flag import FlagSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.flag_status import FlagStatus
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.complex_types.flag_category import FlagCategory
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.complex_types.flag_code import FlagCode
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.plan_definition import PlanDefinition
    from spark_auto_mapper_fhir.resources.medication import Medication
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for author
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Flag(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: FlagStatus,
        category: Optional[FhirList[CodeableConcept[FlagCategory]]] = None,
        code: CodeableConcept[FlagCode],
        subject: Reference[
            Union[
                Patient,
                Location,
                Group,
                Organization,
                Practitioner,
                PlanDefinition,
                Medication,
                Procedure,
            ]
        ],
        period: Optional[Period] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        author: Optional[
            Reference[
                Union[Device, Organization, Patient, Practitioner, PractitionerRole]
            ]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifiers assigned to this flag by the performer or other systems
        which remain constant as the resource is updated and propagates from server to
        server.
            :param status: Supports basic workflow.
            :param category: Allows a flag to be divided into different categories like clinical,
        administrative etc. Intended to be used as a means of filtering which flags
        are displayed to particular user or in a given context.
            :param code: The coded value or textual component of the flag to display to the user.
            :param subject: The patient, location, group, organization, or practitioner etc. this is about
        record this flag is associated with.
            :param period: The period of time from the activation of the flag to inactivation of the
        flag. If the flag is active, the end of the period should be unspecified.
            :param encounter: This alert is only relevant during the encounter.
            :param author: The person, organization or device that created the flag.
        """
        super().__init__(
            resourceType="Flag",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            category=category,
            code=code,
            subject=subject,
            period=period,
            encounter=encounter,
            author=author,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return FlagSchema.get_schema(include_extension=include_extension)