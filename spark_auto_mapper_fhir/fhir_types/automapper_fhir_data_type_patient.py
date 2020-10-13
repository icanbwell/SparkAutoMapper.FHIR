from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType
from spark_auto_mapper.helpers.value_parser import AutoMapperValueParser
from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhirDataTypePatient(AutoMapperFhirDataTypeComplexBase):
    # noinspection PyPep8Naming
    def __init__(self,
                 id_: AutoMapperTextInputType,
                 birthDate: AutoMapperDateDataType,
                 name: AutoMapperDataTypeList,
                 gender: AutoMapperTextInputType
                 ) -> None:
        super().__init__()
        self.value = dict(
            id=AutoMapperValueParser.parse_value(id_),
            birthDate=AutoMapperValueParser.parse_value(birthDate),
            name=AutoMapperValueParser.parse_value(name),
            gender=AutoMapperValueParser.parse_value(gender)
        )
