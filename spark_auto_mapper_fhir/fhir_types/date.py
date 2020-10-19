from typing import Union

from spark_auto_mapper.data_types.date import AutoMapperDateDataType
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType

FhirDate = Union[AutoMapperDateInputType, AutoMapperDateDataType]
