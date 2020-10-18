from typing import TypeVar, Generic

from spark_auto_mapper.data_types.list import AutoMapperDataTypeList

_T = TypeVar("_T")


class FhirList(Generic[_T], AutoMapperDataTypeList[_T]):
    pass
