from datetime import date, datetime
from typing import Optional, List, Union

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import lit
from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


class FhirValueSetBase(AutoMapperDataTypeBase):
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__()
        self.value: AutoMapperTextInputType = value

    def get_column_spec(
        self,
        source_df: Optional[DataFrame],
        current_column: Optional[Column],
        parent_columns: Optional[List[Column]],
    ) -> Column:
        if (
            isinstance(self.value, str)
            or isinstance(self.value, int)
            or isinstance(self.value, float)
            or isinstance(self.value, date)
            or isinstance(self.value, datetime)
        ):
            return lit(self.value)

        if isinstance(self.value, AutoMapperDataTypeBase):
            return self.value.get_column_spec(
                source_df=source_df,
                current_column=current_column,
                parent_columns=parent_columns,
            )

        raise ValueError(f"value: {self.value} is not str or AutoMapperDataTypeBase")

    @property
    def children(
        self,
    ) -> Union[AutoMapperDataTypeBase, List[AutoMapperDataTypeBase]]:
        return self.value if isinstance(self.value, AutoMapperDataTypeBase) else []
