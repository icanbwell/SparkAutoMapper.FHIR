from typing import List, Union, Dict, Optional

from pyspark.sql import DataFrame, Column
from spark_auto_mapper.automapper_base import AutoMapperBase
from spark_auto_mapper.automapper_with_column import AutoMapperWithColumn

from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperWithResource(AutoMapperBase):
    def __init__(self,
                 parent: AutoMapperBase,
                 resource: AutoMapperFhirDataTypeComplexBase
                 ) -> None:
        super().__init__(parent=parent)

        self.resource: AutoMapperFhirDataTypeComplexBase = resource

        # set up a bunch of withColumn for each parameter to AutoMapperFhirDataTypeComplexBase
        self.mappers: List[AutoMapperWithColumn] = []
        automapper: Union[AutoMapperWithColumn, AutoMapperWithResource] = self
        for column, value in self.resource.value.items():
            automapper = AutoMapperWithColumn(
                parent=automapper,
                dst_column=column,
                value=value
            )
            assert isinstance(automapper, AutoMapperWithColumn)
            self.mappers.append(automapper)

    def transform_with_data_frame(self, df: DataFrame, source_df: DataFrame, keys: List[str]) -> DataFrame:
        return df  # we do nothing since self.mappers do all the work

    def get_column_specs(self) -> Dict[str, Column]:
        return {mapper.dst_column: mapper.get_column_spec() for mapper in self.mappers}

    def transform(self, df: DataFrame) -> DataFrame:
        # TODO: this is copied from AutoMapperWithColumn.  Figure out a base class to share
        # find the top most AutoMapper which has the information we need
        auto_mapper: Optional[AutoMapperBase] = self
        while auto_mapper and auto_mapper.parent:
            auto_mapper = auto_mapper.parent

        assert auto_mapper
        assert auto_mapper.keys
        source_df: DataFrame = df.sql_ctx.table(auto_mapper.source_view)
        destination_df: DataFrame = source_df.select(auto_mapper.keys)
        # start with the last mapper
        return self.mappers[-1].transform_with_data_frame(df=destination_df, source_df=source_df, keys=auto_mapper.keys)
