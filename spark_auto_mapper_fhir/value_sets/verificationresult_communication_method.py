from __future__ import annotations
from typing import Optional, Union, List, Any, TYPE_CHECKING

from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Verificationresult_communication_method(FhirValueSetBase):
    """
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class Verificationresult_communication_methodValues:
    Manual = Verificationresult_communication_method("manual")
    Portal = Verificationresult_communication_method("portal")
    Pull = Verificationresult_communication_method("pull")
    Push = Verificationresult_communication_method("push")