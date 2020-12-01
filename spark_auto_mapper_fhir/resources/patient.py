from typing import Optional, Union

from pyspark.sql.types import StructType
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase
from spark_fhir_schemas.r4.resources.patient import PatientSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.resources.communication import Communication
from spark_auto_mapper_fhir.complex_types.contact import Contact
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.link_patient import LinkPatient
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.valuesets.marital_status import MaritalStatusCode


class Patient(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        name: Optional[FhirList[HumanName]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        deceasedBoolean: Optional[FhirBoolean] = None,
        deceasedDateTime: Optional[FhirDateTime] = None,
        address: Optional[FhirList[Address]] = None,
        maritalStatus: Optional[CodeableConcept[MaritalStatusCode]] = None,
        multipleBirthBoolean: Optional[FhirBoolean] = None,
        multipleBirthInteger: Optional[FhirPositiveInt] = None,
        photo: Optional[FhirList[Attachment]] = None,
        contact: Optional[FhirList[Contact]] = None,
        communication: Optional[FhirList[Communication]] = None,
        generalPractitioner: Optional[FhirList[Reference[Union[
            Organization, Practitioner, PractitionerRole]]]] = None,
        managingOrganization: Optional[Reference[Organization]] = None,
        link: Optional[FhirList[LinkPatient]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Patient Resource in FHIR
        https://hl7.org/FHIR/patient.html
        Information about an individual or animal receiving health care services


        :param id_: id of resource
        :param identifier: An identifier for this patient
        :param active: Whether this patient's record is in active use
        :param name: A name associated with the patient
        :param telecom: A contact detail for the individual
        :param gender: 	male | female | other | unknown (https://hl7.org/FHIR/valueset-administrative-gender.html)
        :param birthDate: The date of birth for the individual
        :param deceasedBoolean: Indicates if the individual is deceased or not
        :param deceasedDateTime: Indicates if the individual is deceased or not
        :param address: An address for the individual
        :param maritalStatus: Marital (civil) status of a patient (https://hl7.org/FHIR/valueset-marital-status.html)
        :param multipleBirthBoolean: Whether patient is part of a multiple birth
        :param multipleBirthInteger: Whether patient is part of a multiple birth
        :param photo: Image of the patient
        :param contact: A contact party (e.g. guardian, partner, friend) for the patient
                        + Rule: SHALL at least contain a contact's details or a reference to an organization
        :param communication: A language which may be used to communicate with the patient about his or her health
        :param generalPractitioner: Patient's nominated primary care provider
        :param managingOrganization: Organization that is the custodian of the patient record
        :param link: Link to another patient resource that concerns the same actual person
        :param extension: extensions
        """
        super().__init__(
            resourceType="Patient",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            name=name,
            telecom=telecom,
            gender=gender,
            birthDate=birthDate,
            deceasedBoolean=deceasedBoolean,
            deceasedDateTime=deceasedDateTime,
            address=address,
            maritalStatus=maritalStatus,
            multipleBirthBoolean=multipleBirthBoolean,
            multipleBirthInteger=multipleBirthInteger,
            photo=photo,
            contact=contact,
            communication=communication,
            generalPractitioner=generalPractitioner,
            managingOrganization=managingOrganization,
            link=link
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return PatientSchema.get_schema(include_extension=include_extension)

    id_: FhirId = FhirId(A.column("id_"))
    identifier = A.column("identifier")
    active = A.boolean(A.column("active"))
    name = A.column("name")
    telecom = A.column("telecom")
    gender: AutoMapperTextLikeBase = A.column("gender")
    birthDate: AutoMapperDateDataType = A.date(A.column("birthDate"))
    deceasedBoolean = A.column("deceasedBoolean")
    deceasedDateTime = A.column("deceasedDateTime")
    address = A.column("address")
    maritalStatus: AutoMapperTextLikeBase = A.column("maritalStatus")
    multipleBirthBoolean = A.column("multipleBirthBoolean")
    multipleBirthInteger = A.column("multipleBirthInteger")
    photo = A.column("photo")
    contact = A.column("contact")
    communication = A.column("communication")
    generalPractitioner = A.column("generalPractitioner")
    managingOrganization = A.column("managingOrganization")
    link = A.column("link")
