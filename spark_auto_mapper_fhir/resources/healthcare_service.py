from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.healthcareservice import HealthcareServiceSchema

from spark_auto_mapper_fhir.backbone_elements.eligibility_backbone_element import (
    EligibilityBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.not_available_backbone_element import (
    NotAvailableBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.practitioner_available_time_backbone_element import (
    PractitionerAvailableTimeBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode
from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode
from spark_auto_mapper_fhir.valuesets.program import ProgramCode
from spark_auto_mapper_fhir.valuesets.referral_method import ReferralMethodCode
from spark_auto_mapper_fhir.valuesets.service_category import ServiceCategoryCode
from spark_auto_mapper_fhir.valuesets.service_provision_condition import (
    ServiceProvisionConditionCode,
)
from spark_auto_mapper_fhir.valuesets.service_type import ServiceTypeCode


class HealthcareService(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        providedBy: Optional[Reference[Organization]] = None,
        category: Optional[FhirList[CodeableConcept[ServiceCategoryCode]]] = None,
        type_: Optional[FhirList[CodeableConcept[ServiceTypeCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]] = None,
        location: Optional[FhirList[Reference[Location]]] = None,
        name: Optional[FhirString] = None,
        comment: Optional[FhirString] = None,
        extraDetails: Optional[FhirMarkdown] = None,
        photo: Optional[Attachment] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        coverageArea: Optional[FhirList[Reference[Location]]] = None,
        serviceProvisionCode: Optional[
            FhirList[CodeableConcept[ServiceProvisionConditionCode]]
        ] = None,
        eligibility: Optional[FhirList[EligibilityBackboneElement]] = None,
        program: Optional[FhirList[CodeableConcept[ProgramCode]]] = None,
        characteristic: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        communication: Optional[FhirList[CodeableConcept[CommonLanguageCode]]] = None,
        referralMethod: Optional[FhirList[CodeableConcept[ReferralMethodCode]]] = None,
        appointmentRequired: Optional[FhirBoolean] = None,
        availableTime: Optional[
            FhirList[PractitionerAvailableTimeBackboneElement]
        ] = None,
        notAvailable: Optional[FhirList[NotAvailableBackboneElement]] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Endpoint]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        HealthcareService Resource in FHIR
        https://hl7.org/FHIR/healthcareservice.html
        The details of a healthcare service available at a location

        :param id_: id of resource
        :param identifier: External identifiers for this item
        :param active: Whether this HealthcareService record is in active use
        :param providedBy: Organization that provides this service
        :param category: Broad category of service being performed or delivered
        :param type_: Type of service that may be delivered or performed
        :param specialty: Specialties handled by the HealthcareService
        :param location: Location(s) where service may be provided
        :param name: Description of service as presented to a consumer while searching
        :param comment: Additional description and/or any specific issues not covered elsewhere
        :param extraDetails: Extra details about the service that can't be placed in the other fields
        :param photo: Facilitates quick identification of the service
        :param telecom: Contacts related to the healthcare service
        :param coverageArea: Location(s) service is intended for/available to
        :param serviceProvisionCode: Conditions under which service is available/offered
        :param eligibility: Specific eligibility requirements required to use the service
        :param program: Programs that this service is applicable to
        :param characteristic: Collection of characteristics (attributes)
        :param communication: The language that this service is offered in
        :param referralMethod: Ways that the service accepts referrals
        :param appointmentRequired: If an appointment is required for access to this service
        :param availableTime: Times the Service Site is available
        :param notAvailable: Not available during this time due to provided reason
        :param availabilityExceptions: Description of availability exceptions
        :param endpoint: Technical endpoints providing access to electronic services operated for the healthcare service
        """
        super().__init__(
            resourceType="HealthcareService",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            providedBy=providedBy,
            category=category,
            type_=type_,
            specialty=specialty,
            location=location,
            name=name,
            comment=comment,
            extraDetails=extraDetails,
            photo=photo,
            telecom=telecom,
            coverageArea=coverageArea,
            serviceProvisionCode=serviceProvisionCode,
            eligibility=eligibility,
            program=program,
            characteristic=characteristic,
            communication=communication,
            referralMethod=referralMethod,
            appointmentRequired=appointmentRequired,
            availableTime=availableTime,
            notAvailable=notAvailable,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return HealthcareServiceSchema.get_schema(include_extension=include_extension)
