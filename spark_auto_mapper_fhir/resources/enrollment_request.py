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
from spark_fhir_schemas.r4.resources.enrollmentrequest import EnrollmentRequestSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.financial_resource_status_codes import (
        FinancialResourceStatusCodes,
    )
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for insurer
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for candidate
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for coverage
    from spark_auto_mapper_fhir.resources.coverage import Coverage


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EnrollmentRequest(FhirResourceBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: Optional[FinancialResourceStatusCodes] = None,
        created: Optional[FhirDateTime] = None,
        insurer: Optional[Reference[Union[Organization]]] = None,
        provider: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        candidate: Optional[Reference[Union[Patient]]] = None,
        coverage: Optional[Reference[Union[Coverage]]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param identifier: The Response business identifier.
        :param status: The status of the resource instance.
        :param created: The date when this resource was created.
        :param insurer: The Insurer who is target  of the request.
        :param provider: The practitioner who is responsible for the services rendered to the patient.
        :param candidate: Patient Resource.
        :param coverage: Reference to the program or plan identification, underwriter or payor.
        """
        super().__init__(
            resourceType="EnrollmentRequest",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            created=created,
            insurer=insurer,
            provider=provider,
            candidate=candidate,
            coverage=coverage,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EnrollmentRequestSchema.get_schema(include_extension=include_extension)