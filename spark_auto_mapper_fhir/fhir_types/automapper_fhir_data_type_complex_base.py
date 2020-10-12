from typing import Dict

from pyspark.sql import Column
from pyspark.sql.functions import struct
from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class AutoMapperFhirDataTypeComplexBase(AutoMapperDataTypeComplexBase):
    def __init__(self) -> None:
        super().__init__()
        self.value: Dict[str, AutoMapperDataTypeBase] = {}

    def get_column_spec(self) -> Column:
        return struct(
            [
                self.get_value(value).alias(key)
                for key, value in self.value.items()
            ]
        )
