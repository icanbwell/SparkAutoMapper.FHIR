from typing import Union, Optional

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import round
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

    def get_column_spec(
        self, source_df: DataFrame, current_column: Optional[Column]
    ) -> Column:
        column_spec = round(
            self.column.get_column_spec(
                source_df=source_df, current_column=current_column
            ).cast("float"), 6
        )
        return column_spec
