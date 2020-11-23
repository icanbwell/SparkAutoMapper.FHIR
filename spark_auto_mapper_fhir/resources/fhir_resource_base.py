from typing import Optional

from pyspark.sql.types import StructType
from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase


class FhirResourceBase(AutoMapperDataTypeComplexBase):
    # all resources must implement this
    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        raise NotImplementedError
