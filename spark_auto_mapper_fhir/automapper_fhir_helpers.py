from spark_auto_mapper.data_types.automapper_defined_types import AutoMapperTextType
from spark_auto_mapper.data_types.automapper_data_type_date import AutoMapperDataTypeDate
from spark_auto_mapper.data_types.automapper_data_type_list import AutoMapperDataTypeList
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient


class AutoMapperFhirHelpers:
    # noinspection PyPep8Naming
    @staticmethod
    def patient(id_: AutoMapperTextType,
                birthDate: AutoMapperDataTypeDate,
                name: AutoMapperDataTypeList,
                gender: AutoMapperTextType
                ) -> AutoMapperFhirDataTypePatient:
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            birthDate=birthDate,
            name=name,
            gender=gender
        )

    @staticmethod
    def human_name(use: AutoMapperTextType,
                   family: AutoMapperTextType
                   ) -> AutoMapperFhirDataTypeHumanName:
        return AutoMapperFhirDataTypeHumanName(
            use=use,
            family=family
        )
