from typing import Optional

from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.code import AutoMapperFhirCodeInputType
from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import AutoMapperFhirDataTypeIdentifier


class AutoMapperFhirDataTypePatient(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            id_: AutoMapperTextInputType,
            identifier: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeIdentifier]] = None,
            birthDate: Optional[AutoMapperDateDataType] = None,
            name: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeHumanName]] = None,
            gender: Optional[AutoMapperFhirCodeInputType] = None,
            address: Optional[AutoMapperDataTypeList] = None,
            maritalStatus: Optional[AutoMapperFhirDataTypeCodeableConcept] = None
            ) -> 'AutoMapperFhirDataTypePatient':
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
        """
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            identifier=identifier,
            birthDate=birthDate,
            name=name,
            gender=gender,
            address=address,
            maritalStatus=maritalStatus
        )

    birthDate: AutoMapperDateDataType = A.date(A.column("birthDate"))
    gender: AutoMapperDataTypeColumn = A.column("gender")
    maritalStatus: AutoMapperDataTypeColumn = A.column("maritalStatus")
