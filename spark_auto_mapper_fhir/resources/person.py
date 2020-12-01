from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.person import PersonSchema

from spark_auto_mapper_fhir.backbone_elements.link_person_backbone_element import LinkPersonBackboneElement
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode


class Person(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        name: Optional[FhirList[HumanName]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        address: Optional[FhirList[Address]] = None,
        photo: Optional[Attachment] = None,
        managingOrganization: Optional[Reference[Organization]] = None,
        active: Optional[FhirBoolean] = None,
        link: Optional[FhirList[LinkPersonBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Person Resource in FHIR
        https://hl7.org/FHIR/person.html#Person
        A generic person record


        :param id_: id of resource
        :param identifier: A human identifier for this person
        :param name: A name associated with the person
        :param telecom: A contact detail for the person
        :param gender: male | female | other | unknown
        :param birthDate: The date on which the person was born
        :param address: One or more addresses for the person
        :param photo: Image of the person
        :param managingOrganization: The organization that is the custodian of the person record
        :param active: This person's record is in active use
        :param link: Link to a resource that concerns the same actual person
        """
        super().__init__(
            resourceType="Person",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            name=name,
            telecom=telecom,
            gender=gender,
            birthDate=birthDate,
            address=address,
            photo=photo,
            managingOrganization=managingOrganization,
            active=active,
            link=link,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return PersonSchema.get_schema(include_extension=include_extension)
