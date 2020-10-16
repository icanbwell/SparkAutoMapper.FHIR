from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.helpers.value_parser import AutoMapperValueParser
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


class AutoMapperFhirDataTypePatient(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    def __init__(self,
                 **kwargs
                 ) -> None:
        super().__init__()
        self.value = {
            parameter_name if parameter_name != "id_" else "id": AutoMapperValueParser.parse_value(parameter_value)
            for parameter_name, parameter_value
            in kwargs.items()
            if parameter_value is not None
        }

    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            id_: AutoMapperTextInputType,
            birthDate: AutoMapperDateDataType,
            name: AutoMapperDataTypeList,
            gender: AutoMapperTextInputType
            ) -> 'AutoMapperFhirDataTypePatient':
        """
        Patient Resource in FHIR
        https://hl7.org/FHIR/patient.html


        :param id_: id of resource
        :param birthDate: The date of birth for the individual
        :param name: A name associated with the patient
        :param gender: 	male | female | other | unknown (https://hl7.org/FHIR/valueset-administrative-gender.html)
        """
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            birthDate=birthDate,
            name=name,
            gender=gender
        )
