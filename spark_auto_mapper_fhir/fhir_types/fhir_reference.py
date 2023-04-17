from typing import Union, Optional, List

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import lit
from pyspark.sql.functions import concat
from spark_auto_mapper.data_types.column import AutoMapperDataTypeColumn
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId


class FhirReference(AutoMapperTextLikeBase):
    """
    Cleans up the text for an id column
    """

    def __init__(
        self,
        resource: str,
        column: Union[AutoMapperDataTypeColumn, AutoMapperTextLikeBase],
    ):
        super().__init__()

        assert resource
        assert "/" not in resource
        self.resource: str = resource
        self.column: Union[AutoMapperDataTypeColumn, AutoMapperTextLikeBase] = FhirId(
            column, is_reference=True
        )

    def get_column_spec(
        self,
        source_df: Optional[DataFrame],
        current_column: Optional[Column],
        parent_columns: Optional[List[Column]],
    ) -> Column:
        # https://hl7.org/FHIR/datatypes.html#id
        column_spec = concat(
            lit(self.resource),
            lit("/"),
            self.column.get_column_spec(
                source_df=source_df,
                current_column=current_column,
                parent_columns=parent_columns,
            ),
        )
        return column_spec
