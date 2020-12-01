from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.practitionerrole import PractitionerRoleSchema

from spark_auto_mapper_fhir.backbone_elements.not_available_backbone_element import NotAvailableBackboneElement
from spark_auto_mapper_fhir.backbone_elements.practitioner_available_time_backbone_element import \
    PractitionerAvailableTimeBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode
from spark_auto_mapper_fhir.valuesets.practitioner_role import PractitionerRoleCode


class PractitionerRole(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
        practitioner: Optional[Reference[Practitioner]] = None,
        organization: Optional[Reference[Organization]] = None,
        code: Optional[FhirList[CodeableConcept[PractitionerRoleCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]
                            ] = None,
        location: Optional[FhirList[Reference[Location]]] = None,
        healthcareService: Optional[FhirList[Reference[HealthcareService]]
                                    ] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        availableTime: Optional[
            FhirList[PractitionerAvailableTimeBackboneElement]] = None,
        notAvailable: Optional[FhirList[NotAvailableBackboneElement]] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Endpoint]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        PractitionerRole Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#PractitionerRole
        Roles/organizations the practitioner is associated with


        :param id_: id of resource
        :param identifier: Business Identifiers that are specific to a role/location
        :param active: Whether this practitioner role record is in active use
        :param period: The period during which the practitioner is authorized to perform in these role(s)
        :param practitioner: Practitioner that is able to provide the defined services for the organization
        :param organization: Organization where the roles are available
        :param code: Roles which this practitioner may perform
        :param specialty: Specific specialty of the practitioner
        :param location: The location(s) at which this practitioner provides care
        :param healthcareService: The list of healthcare services that this worker provides for this role's Organization/Location(s)
        :param telecom: Contact details that are specific to the role/location/service
        :param availableTime: Times the Service Site is available
        :param notAvailable: Not available during this time due to provided reason
        :param availabilityExceptions: Description of availability exceptions
        :param endpoint: Technical endpoints providing access to services operated for the practitioner with this role
        """
        super().__init__(
            resourceType="PractitionerRole",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            period=period,
            practitioner=practitioner,
            organization=organization,
            code=code,
            specialty=specialty,
            location=location,
            healthcareService=healthcareService,
            telecom=telecom,
            availableTime=availableTime,
            notAvailable=notAvailable,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return PractitionerRoleSchema.get_schema(
            include_extension=include_extension
        )
