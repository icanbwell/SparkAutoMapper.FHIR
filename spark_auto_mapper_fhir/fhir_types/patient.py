from typing import Optional, Union

from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.communication import FhirCommunication
from spark_auto_mapper_fhir.fhir_types.contact import FhirContact
from spark_auto_mapper_fhir.fhir_types.contact_point import FhirContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.link_patient import FhirLinkPatient
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import FhirAdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.marital_status import FhirMaritalStatusCode


class FhirPatient(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        id_: Optional[FhirId] = None,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        active: Optional[FhirBoolean] = None,
        name: Optional[FhirList[FhirHumanName]] = None,
        telecom: Optional[FhirList[FhirContactPoint]] = None,
        gender: Optional[FhirAdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        deceasedBoolean: Optional[FhirBoolean] = None,
        deceasedDateTime: Optional[FhirDateTime] = None,
        address: Optional[FhirList[FhirAddress]] = None,
        maritalStatus: Optional[FhirCodeableConcept[FhirMaritalStatusCode]
                                ] = None,
        multipleBirthBoolean: Optional[FhirBoolean] = None,
        multipleBirthInteger: Optional[FhirPositiveInt] = None,
        photo: Optional[FhirList[FhirAttachment]] = None,
        contact: Optional[FhirList[FhirContact]] = None,
        communication: Optional[FhirList[FhirCommunication]] = None,
        generalPractitioner: Optional[FhirList[FhirReference[
            Union[FhirOrganization, FhirPractitioner,
                  FhirPractitionerRole]]]] = None,
        managingOrganization: Optional[FhirReference[FhirOrganization]] = None,
        link: Optional[FhirList[FhirLinkPatient]] = None
    ) -> 'FhirPatient':
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
        """
        return FhirPatient(
            id_=id_,
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

    id_: AutoMapperDataTypeColumn = A.column("id_")
    identifier = A.column("identifier")
    active = A.boolean(A.column("active"))
    name = A.column("name")
    telecom = A.column("telecom")
    gender: AutoMapperDataTypeColumn = A.column("gender")
    birthDate: AutoMapperDateDataType = A.date(A.column("birthDate"))
    deceasedBoolean = A.column("deceasedBoolean")
    deceasedDateTime = A.column("deceasedDateTime")
    address = A.column("address")
    maritalStatus: AutoMapperDataTypeColumn = A.column("maritalStatus")
    multipleBirthBoolean = A.column("multipleBirthBoolean")
    multipleBirthInteger = A.column("multipleBirthInteger")
    photo = A.column("photo")
    contact = A.column("contact")
    communication = A.column("communication")
    generalPractitioner = A.column("generalPractitioner")
    managingOrganization = A.column("managingOrganization")
    link = A.column("link")
