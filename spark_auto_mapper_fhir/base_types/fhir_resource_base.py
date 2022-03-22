from typing import Optional, Union, List

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)


class FhirResourceBase(AutoMapperDataTypeComplexBase):
    # all resources must implement this
    def get_schema(
        self, include_extension: bool, extension_fields: Optional[List[str]] = None
    ) -> Optional[Union[StructType, DataType]]:
        raise NotImplementedError
