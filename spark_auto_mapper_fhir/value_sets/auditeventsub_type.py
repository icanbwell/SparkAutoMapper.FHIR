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
class Auditeventsub_type(FhirValueSetBase):
    """
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class Auditeventsub_typeValues:
    _110120 = Auditeventsub_type("110120")
    _110121 = Auditeventsub_type("110121")
    _110122 = Auditeventsub_type("110122")
    _110123 = Auditeventsub_type("110123")
    _110124 = Auditeventsub_type("110124")
    _110125 = Auditeventsub_type("110125")
    _110126 = Auditeventsub_type("110126")
    _110127 = Auditeventsub_type("110127")
    _110128 = Auditeventsub_type("110128")
    _110129 = Auditeventsub_type("110129")
    _110130 = Auditeventsub_type("110130")
    _110131 = Auditeventsub_type("110131")
    _110132 = Auditeventsub_type("110132")
    _110133 = Auditeventsub_type("110133")
    _110134 = Auditeventsub_type("110134")
    _110135 = Auditeventsub_type("110135")
    _110136 = Auditeventsub_type("110136")
    _110137 = Auditeventsub_type("110137")
    _110138 = Auditeventsub_type("110138")
    _110139 = Auditeventsub_type("110139")
    _110140 = Auditeventsub_type("110140")
    _110141 = Auditeventsub_type("110141")
    _110142 = Auditeventsub_type("110142")