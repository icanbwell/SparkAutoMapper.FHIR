from typing import Optional

from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


class AutoMapperFhirDataTypePatient(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            id_: AutoMapperTextInputType,
            birthDate: AutoMapperDateDataType,
            name: AutoMapperDataTypeList,
            gender: AutoMapperTextInputType,
            address: Optional[AutoMapperDataTypeList] = None
            ) -> 'AutoMapperFhirDataTypePatient':
        """
        Patient Resource in FHIR
        https://hl7.org/FHIR/patient.html


        :param id_: id of resource
        :param birthDate: The date of birth for the individual
        :param name: A name associated with the patient
        :param gender: 	male | female | other | unknown (https://hl7.org/FHIR/valueset-administrative-gender.html)
        :param address: An address for the individual
        """
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            birthDate=birthDate,
            name=name,
            gender=gender,
            address=address
        )

    birthDate: AutoMapperDataTypeColumn = A.column("birthDate")
    gender: AutoMapperTextInputType = A.column("gender")
