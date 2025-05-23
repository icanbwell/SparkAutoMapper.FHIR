from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.practitionerrole import PractitionerRoleSchema

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # active (boolean)
    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # practitioner (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for practitioner
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner

    # organization (Reference)
    # Imports for References for organization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.practitioner_role import PractitionerRoleCode

    # End Import for CodeableConcept for code
    # specialty (CodeableConcept)
    # Import for CodeableConcept for specialty
    from spark_auto_mapper_fhir.value_sets.practice_setting_code_value_set import (
        PracticeSettingCodeValueSetCode,
    )

    # End Import for CodeableConcept for specialty
    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # healthcareService (Reference)
    # Imports for References for healthcareService
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # availableTime (PractitionerRole.AvailableTime)
    from spark_auto_mapper_fhir.backbone_elements.practitioner_role_available_time import (
        PractitionerRoleAvailableTime,
    )

    # notAvailable (PractitionerRole.NotAvailable)
    from spark_auto_mapper_fhir.backbone_elements.practitioner_role_not_available import (
        PractitionerRoleNotAvailable,
    )

    # availabilityExceptions (string)
    # endpoint (Reference)
    # Imports for References for endpoint
    from spark_auto_mapper_fhir.resources.endpoint import Endpoint


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PractitionerRole(FhirResourceBase):
    """
    PractitionerRole
    practitionerrole.xsd
        A specific set of Roles/Locations/specialties/services that a practitioner may
    perform at an organization for a period of time.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        use_date_for: Optional[List[str]] = None,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
        practitioner: Optional[Reference[Practitioner]] = None,
        organization: Optional[Reference[Organization]] = None,
        code: Optional[FhirList[CodeableConcept[PractitionerRoleCode]]] = None,
        specialty: Optional[
            FhirList[CodeableConcept[PracticeSettingCodeValueSetCode]]
        ] = None,
        location: Optional[FhirList[Reference[Location]]] = None,
        healthcareService: Optional[FhirList[Reference[HealthcareService]]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        availableTime: Optional[FhirList[PractitionerRoleAvailableTime]] = None,
        notAvailable: Optional[FhirList[PractitionerRoleNotAvailable]] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
    ) -> None:
        """
            A specific set of Roles/Locations/specialties/services that a practitioner may
        perform at an organization for a period of time.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param identifier: Business Identifiers that are specific to a role/location.
            :param active: Whether this practitioner role record is in active use.
            :param period: The period during which the person is authorized to act as a practitioner in
        these role(s) for the organization.
            :param practitioner: Practitioner that is able to provide the defined services for the
        organization.
            :param organization: The organization where the Practitioner performs the roles associated.
            :param code: Roles which this practitioner is authorized to perform for the organization.
            :param specialty: Specific specialty of the practitioner.
            :param location: The location(s) at which this practitioner provides care.
            :param healthcareService: The list of healthcare services that this worker provides for this role's
        Organization/Location(s).
            :param telecom: Contact details that are specific to the role/location/service.
            :param availableTime: A collection of times the practitioner is available or performing this role at
        the location and/or healthcareservice.
            :param notAvailable: The practitioner is not available or performing this role during this period
        of time due to the provided reason.
            :param availabilityExceptions: A description of site availability exceptions, e.g. public holiday
        availability. Succinctly describing all possible exceptions to normal site
        availability as details in the available Times and not available Times.
            :param endpoint: Technical endpoints providing access to services operated for the practitioner
        with this role.
        """
        super().__init__(
            resourceType="PractitionerRole",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
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

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return PractitionerRoleSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
