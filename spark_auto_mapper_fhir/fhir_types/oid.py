from typing import Union

from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

FhirOid = Union[AutoMapperTextInputType, AutoMapperTextLikeBase]
