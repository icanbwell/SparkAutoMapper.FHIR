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
from spark_fhir_schemas.r4.resources.enrollmentresponse import EnrollmentResponseSchema

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier
    from spark_auto_mapper_fhir.complex_types.financial_resource_status_codes import (
        FinancialResourceStatusCodes,
    )
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for request
    from spark_auto_mapper_fhir.resources.enrollment_request import EnrollmentRequest
    from spark_auto_mapper_fhir.complex_types.remittance_outcome import (
        RemittanceOutcome,
    )
    from spark_auto_mapper_fhir.complex_types.string import FhirString
    from spark_auto_mapper_fhir.complex_types.date_time import FhirDateTime
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for organization
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for requestProvider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EnrollmentResponse(FhirResourceBase):
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
        request: Optional[Reference[Union[EnrollmentRequest]]] = None,
        outcome: Optional[RemittanceOutcome] = None,
        disposition: Optional[FhirString] = None,
        created: Optional[FhirDateTime] = None,
        organization: Optional[Reference[Union[Organization]]] = None,
        requestProvider: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param identifier: The Response business identifier.
        :param status: The status of the resource instance.
        :param request: Original request resource reference.
        :param outcome: Processing status: error, complete.
        :param disposition: A description of the status of the adjudication.
        :param created: The date when the enclosed suite of services were performed or completed.
        :param organization: The Insurer who produced this adjudicated response.
        :param requestProvider: The practitioner who is responsible for the services rendered to the patient.
        """
        super().__init__(
            resourceType="EnrollmentResponse",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            request=request,
            outcome=outcome,
            disposition=disposition,
            created=created,
            organization=organization,
            requestProvider=requestProvider,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EnrollmentResponseSchema.get_schema(include_extension=include_extension)