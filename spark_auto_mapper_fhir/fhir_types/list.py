from typing import TypeVar, Union, Optional, List

from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.data_types.list import AutoMapperList
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

# https://mypy.readthedocs.io/en/stable/generics.html
_T = TypeVar(
    "_T", bound=Union[AutoMapperNativeSimpleType, AutoMapperDataTypeBase]
)


class FhirList(AutoMapperList[_T]):
    def __init__(self, value: Optional[List[_T]]) -> None:
        super().__init__(value=value)

        # TODO: check if value is a list of struct that we have the same columns in each
        #   otherwise Spark will complain
