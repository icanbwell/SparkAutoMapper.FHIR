from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_human_name import AutoMapperFhirDataTypeHumanName
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_patient import AutoMapperFhirDataTypePatient


class AutoMapperFhirHelpers:
    # noinspection PyPep8Naming
    @staticmethod
    def patient(id_: AutoMapperTextInputType,
                birthDate: AutoMapperDateDataType,
                name: AutoMapperDataTypeList,
                gender: AutoMapperTextInputType
                ) -> AutoMapperFhirDataTypePatient:
        return AutoMapperFhirDataTypePatient(
            id_=id_,
            birthDate=birthDate,
            name=name,
            gender=gender
        )

    @staticmethod
    def human_name(use: AutoMapperTextInputType,
                   family: AutoMapperTextInputType
                   ) -> AutoMapperFhirDataTypeHumanName:
        return AutoMapperFhirDataTypeHumanName(
            use=use,
            family=family
        )
