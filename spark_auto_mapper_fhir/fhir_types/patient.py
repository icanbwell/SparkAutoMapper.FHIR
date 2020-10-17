from typing import Optional, Union

from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.practitioner import FhirPractitioner
from spark_auto_mapper_fhir.fhir_types.practitioner_role import FhirPractitionerRole
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirPatient(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            id_: FhirString,
            identifier: Optional[FhirList[FhirIdentifier]] = None,
            birthDate: Optional[FhirDate] = None,
            name: Optional[FhirList[FhirHumanName]] = None,
            gender: Optional[FhirCode] = None,
            address: Optional[FhirList[FhirAddress]] = None,
            maritalStatus: Optional[FhirCodeableConcept] = None,
            generalPractitioner: Optional[FhirList[
                FhirReference[
                    Union[
                        FhirOrganization,
                        FhirPractitioner,
                        FhirPractitionerRole
                    ]
                ]
            ]] = None,
            managingOrganization: Optional[FhirReference] = None
            ) -> 'FhirPatient':
        """
        Patient Resource in FHIR
        https://hl7.org/FHIR/patient.html
        Information about an individual or animal receiving health care services


        :param id_: id of resource
        :param identifier: An identifier for this patient
        :param birthDate: The date of birth for the individual
        :param name: A name associated with the patient
        :param gender: 	male | female | other | unknown (https://hl7.org/FHIR/valueset-administrative-gender.html)
        :param address: An address for the individual
        :param maritalStatus: Marital (civil) status of a patient (https://hl7.org/FHIR/valueset-marital-status.html)
        :param generalPractitioner: Patient's nominated primary care provider
        :param managingOrganization: Organization that is the custodian of the patient record
        """
        return FhirPatient(
            id_=id_,
            identifier=identifier,
            birthDate=birthDate,
            name=name,
            gender=gender,
            address=address,
            maritalStatus=maritalStatus,
            generalPractitioner=generalPractitioner,
            managingOrganization=managingOrganization
        )

    birthDate: AutoMapperDateDataType = A.date(A.column("birthDate"))
    gender: AutoMapperDataTypeColumn = A.column("gender")
    maritalStatus: AutoMapperDataTypeColumn = A.column("maritalStatus")
