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
class Procedurefollowupcodes_snomedct_(FhirValueSetBase):
    """
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class Procedurefollowupcodes_snomedct_Values:
    _18949003 = Procedurefollowupcodes_snomedct_("18949003")
    _30549001 = Procedurefollowupcodes_snomedct_("30549001")
    _241031001 = Procedurefollowupcodes_snomedct_("241031001")
    _35963001 = Procedurefollowupcodes_snomedct_("35963001")
    _225164002 = Procedurefollowupcodes_snomedct_("225164002")
    _447346005 = Procedurefollowupcodes_snomedct_("447346005")
    _229506003 = Procedurefollowupcodes_snomedct_("229506003")
    _274441001 = Procedurefollowupcodes_snomedct_("274441001")
    _394725008 = Procedurefollowupcodes_snomedct_("394725008")
    _359825008 = Procedurefollowupcodes_snomedct_("359825008")