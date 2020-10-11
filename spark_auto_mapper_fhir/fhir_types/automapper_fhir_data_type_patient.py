from spark_auto_mapper.automapper_defined_types import AutomapperTextType
from spark_auto_mapper.automapper_value_parser import AutoMapperValueParser
from spark_auto_mapper.data_types.automapper_data_type_date import AutoMapperDataTypeDate
from spark_auto_mapper.data_types.automapper_data_type_list import AutoMapperDataTypeList
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhirDataTypePatient(AutoMapperFhirDataTypeComplexBase):
    # noinspection PyPep8Naming
    def __init__(self,
                 id_: AutomapperTextType,
                 birthDate: AutoMapperDataTypeDate,
                 name: AutoMapperDataTypeList
                 ) -> None:
        super().__init__()
        self.value = dict(
            id=AutoMapperValueParser.parse_value(id_),
            birthDate=AutoMapperValueParser.parse_value(birthDate),
            name=AutoMapperValueParser.parse_value(name)
        )
