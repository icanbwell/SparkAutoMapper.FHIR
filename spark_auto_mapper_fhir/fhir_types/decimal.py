from typing import Union

from pyspark.sql import DataFrame, Column
from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase


class FhirDecimal(AutoMapperTextLikeBase):
    """
    Cleans up the text for an id column
    """
    def __init__(
        self, column: Union[AutoMapperDataTypeColumn, AutoMapperTextLikeBase]
    ):
        super().__init__()

        self.column: Union[AutoMapperDataTypeColumn,
                           AutoMapperTextLikeBase] = column

    def get_column_spec(self, source_df: DataFrame) -> Column:
        column_spec = self.column.get_column_spec(source_df=source_df
                                                  ).cast("float")
        return column_spec
