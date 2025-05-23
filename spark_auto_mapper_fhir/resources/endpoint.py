from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.endpoint import EndpointSchema

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

    # status (EndpointStatus)
    from spark_auto_mapper_fhir.value_sets.endpoint_status import EndpointStatusCode

    # connectionType (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for connectionType
    from spark_auto_mapper_fhir.value_sets.endpoint_connection_type import (
        EndpointConnectionTypeCode,
    )

    # End Import for CodeableConcept for connectionType
    # name (string)
    # managingOrganization (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for managingOrganization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # contact (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # payloadType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for payloadType
    from spark_auto_mapper_fhir.value_sets.endpoint_payload_type import (
        EndpointPayloadTypeCode,
    )

    # End Import for CodeableConcept for payloadType
    # payloadMimeType (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # address (url)
    from spark_auto_mapper_fhir.fhir_types.url import FhirUrl

    # header (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Endpoint(FhirResourceBase):
    """
    Endpoint
    endpoint.xsd
        The technical details of an endpoint that can be used for electronic services,
    such as for web services providing XDS.b or a REST endpoint for another FHIR
    server. This may include any security context information.
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
        status: EndpointStatusCode,
        connectionType: Coding[EndpointConnectionTypeCode],
        name: Optional[FhirString] = None,
        managingOrganization: Optional[Reference[Organization]] = None,
        contact: Optional[FhirList[ContactPoint]] = None,
        period: Optional[Period] = None,
        payloadType: FhirList[CodeableConcept[EndpointPayloadTypeCode]],
        payloadMimeType: Optional[FhirList[MimeTypesCode]] = None,
        address: FhirUrl,
        header: Optional[FhirList[FhirString]] = None,
    ) -> None:
        """
            The technical details of an endpoint that can be used for electronic services,
        such as for web services providing XDS.b or a REST endpoint for another FHIR
        server. This may include any security context information.
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
            :param identifier: Identifier for the organization that is used to identify the endpoint across
        multiple disparate systems.
            :param status: active | suspended | error | off | test.
            :param connectionType: A coded value that represents the technical details of the usage of this
        endpoint, such as what WSDLs should be used in what way. (e.g.
        XDS.b/DICOM/cds-hook).
            :param name: A friendly name that this endpoint can be referred to with.
            :param managingOrganization: The organization that manages this endpoint (even if technically another
        organization is hosting this in the cloud, it is the organization associated
        with the data).
            :param contact: Contact details for a human to contact about the subscription. The primary use
        of this for system administrator troubleshooting.
            :param period: The interval during which the endpoint is expected to be operational.
            :param payloadType: The payload type describes the acceptable content that can be communicated on
        the endpoint.
            :param payloadMimeType: The mime type to send the payload in - e.g. application/fhir+xml,
        application/fhir+json. If the mime type is not specified, then the sender
        could send any content (including no content depending on the connectionType).
            :param address: The uri that describes the actual end-point to connect to.
            :param header: Additional headers / information to send as part of the notification.
        """
        super().__init__(
            resourceType="Endpoint",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            status=status,
            connectionType=connectionType,
            name=name,
            managingOrganization=managingOrganization,
            contact=contact,
            period=period,
            payloadType=payloadType,
            payloadMimeType=payloadMimeType,
            address=address,
            header=header,
        )

        self.use_date_for = use_date_for

    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        return EndpointSchema.get_schema(
            include_extension=include_extension,
            extension_fields=extension_fields,
            use_date_for=self.use_date_for,
        )
