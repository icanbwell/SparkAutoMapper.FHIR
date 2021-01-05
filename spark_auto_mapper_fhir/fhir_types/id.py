from typing import Union, Optional

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import regexp_replace, substring
from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase


class FhirId(AutoMapperTextLikeBase):
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
        # https://hl7.org/FHIR/datatypes.html#id
        column_spec = substring(
            regexp_replace(
                str=self.column.get_column_spec(
                    source_df=source_df, current_column=current_column
                ),
                pattern=r'[^A-Za-z0-9\-\.]',
                replacement="_"
            ), 0, 63
        )
        return column_spec
