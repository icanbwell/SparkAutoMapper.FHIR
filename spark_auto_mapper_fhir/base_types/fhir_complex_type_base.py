from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)


class FhirComplexTypeBase(AutoMapperDataTypeComplexBase):
    # all resources must implement this
    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        raise NotImplementedError
