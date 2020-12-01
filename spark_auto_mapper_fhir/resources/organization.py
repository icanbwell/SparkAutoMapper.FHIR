from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.organization import OrganizationSchema

from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.organization_contact_backbone_element import \
    OrganizationContactBackboneElement
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.organization_type import OrganizationTypeCode


class Organization(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        type_: Optional[FhirList[CodeableConcept[OrganizationTypeCode]]
                        ] = None,
        name: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[FhirList[Address]] = None,
        partOf: Optional[Reference['Organization']] = None,
        contact: Optional[FhirList[OrganizationContactBackboneElement]] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Organization Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Organization
        A grouping of people or organizations with a common purpose
        + Rule: The organization SHALL at least have a name or an identifier, and possibly more than one


        :param id_: id of resource
        :param identifier: Identifies this organization across multiple systems
        :param active: Whether the organization's record is still in active use
        :param type_: Kind of organization. http://hl7.org/fhir/valueset-organization-type.html
        :param name: Name used for the organization
        :param alias: A list of alternate names that the organization is known as, or was known as in the past
        :param telecom: A contact detail for the organization
                        + Rule: The telecom of an organization can never be of use 'home'
        :param address: An address for the organization
                        + Rule: An address of an organization can never be of use 'home'
        :param partOf: The organization of which this organization forms a part
        :param contact: Contact for the organization for a certain purpose
        :param endpoint: Technical endpoints providing access to services operated for the organization
        """
        super().__init__(
            resourceType="Organization",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            type_=type_,
            name=name,
            alias=alias,
            telecom=telecom,
            address=address,
            partOf=partOf,
            contact=contact,
            endpoint=endpoint,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return OrganizationSchema.get_schema(
            include_extension=include_extension
        )
