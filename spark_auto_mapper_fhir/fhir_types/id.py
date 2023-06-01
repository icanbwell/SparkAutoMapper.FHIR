from typing import Union, Optional, List

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import regexp_replace, substring
from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase


class FhirId(AutoMapperTextLikeBase):
    """
    Cleans up the text for an id column
    """

    def __init__(
        self,
        column: Union[AutoMapperDataTypeColumn, AutoMapperTextLikeBase],
        is_reference: Optional[bool] = False,
    ):
        super().__init__()

        self.column: Union[AutoMapperDataTypeColumn, AutoMapperTextLikeBase] = column
        self.is_reference = is_reference

    def get_column_spec(
        self,
        source_df: Optional[DataFrame],
        current_column: Optional[Column],
        parent_columns: Optional[List[Column]],
    ) -> Column:
        # https://hl7.org/FHIR/datatypes.html#id
        column_spec = substring(
            regexp_replace(
                str=self.column.get_column_spec(
                    source_df=source_df,
                    current_column=current_column,
                    parent_columns=parent_columns,
                ),
                pattern=r"[^A-Za-z0-9\|\-\.]"
                if self.is_reference
                else r"[^A-Za-z0-9\-\.]",
                replacement="-",
            ),
            0,
            1024 * 1024,
        )
        return column_spec
