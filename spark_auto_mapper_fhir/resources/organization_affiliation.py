from typing import Optional
from pyspark.sql.types import StructType
from spark_auto_mapper_fhir.resources.endpoint import Endpoint

from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

from spark_auto_mapper_fhir.resources.location import Location

from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.resources.organization import Organization

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.resources.organizationaffiliation import OrganizationAffiliationSchema

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.valuesets.organization_affiliation_role import OrganizationAffiliationRoleCode


class OrganizationAffiliation(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
        organization: Optional[Reference[Organization]] = None,
        participatingOrganization: Optional[Reference[Organization]] = None,
        network: Optional[FhirList[Reference[Organization]]] = None,
        code: Optional[FhirList[
            CodeableConcept[OrganizationAffiliationRoleCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]
                            ] = None,
        location: Optional[FhirList[Reference[Location]]] = None,
        healthcareService: Optional[FhirList[Reference[HealthcareService]]
                                    ] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None
    ) -> None:
        """
        OrganizationAffiliation Resource in FHIR
        https://www.hl7.org/fhir/organizationaffiliation.html
        Defines an affiliation/association/relationship between 2 distinct organizations,
        that is not a part-of relationship/sub-division relationship

        :param id_: id of resource
        :param meta: meta
        :param extension: extension
        :param identifier: Business identifiers that are specific to this role
        :param active: Whether this organization affiliation record is in active use
        :param period: The period during which the participatingOrganization is affiliated with the primary organization
        :param organization: Organization where the role is available
        :param participatingOrganization: Organization that provides/performs the role (e.g. providing services or is a
                                        member of)
        :param network: Health insurance provider network in which the participatingOrganization provides the role's
                        services (if defined) at the indicated locations (if defined)
        :param code: Definition of the role the participatingOrganization plays
        :param specialty: Specific specialty of the participatingOrganization in the context of the role
        :param location: The location(s) at which the role occurs
        :param healthcareService: Healthcare services provided through the role
        :param telecom: Contact details at the participatingOrganization relevant to this Affiliation
        :param endpoint: Technical endpoints providing access to services operated for this role
        """
        super().__init__(
            resourceType="OrganizationAffiliation",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            period=period,
            organization=organization,
            participatingOrganization=participatingOrganization,
            network=network,
            code=code,
            specialty=specialty,
            location=location,
            healthcareService=healthcareService,
            telecom=telecom,
            endpoint=endpoint
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return OrganizationAffiliationSchema.get_schema(
            include_extension=include_extension
        )
