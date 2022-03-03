from typing import Optional, Any

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.time import FhirTime
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.url import FhirUrl
from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode


class NestedExtensionItem(ExtensionBase):
    """
    All nested extensions MUST derive from this class so the default properties are available.  Otherwise, Spark
    complains that some properties are not present in the data frame
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        url: Optional[FhirUri] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueCode: Optional[GenericTypeCode] = None,
        valueDate: Optional[FhirDate] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valueDecimal: Optional[FhirDecimal] = None,
        valueId: Optional[FhirId] = None,
        valueInteger: Optional[FhirInteger] = None,
        valuePositiveInt: Optional[FhirPositiveInt] = None,
        valueString: Optional[FhirString] = None,
        valueTime: Optional[FhirTime] = None,
        valueUnsignedInt: Optional[FhirUnsignedInt] = None,
        valueUri: Optional[FhirUri] = None,
        valueUrl: Optional[FhirUrl] = None,
        include_null_properties: bool = True,
        **kwargs: Any  # allow additional properties
    ) -> None:
        super().__init__(
            id_=id_,
            extension=None,
            url=url,
            valueBoolean=valueBoolean,
            valueCode=valueCode,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueDecimal=valueDecimal,
            valueId=valueId,
            valueInteger=valueInteger,
            valuePositiveInt=valuePositiveInt,
            valueString=valueString,
            valueTime=valueTime,
            valueUnsignedInt=valueUnsignedInt,
            valueUri=valueUri,
            valueUrl=valueUrl,
            **kwargs
        )
        # must set this to true so all null properties are available in the data frame otherwise
        #   Spark will complain
        super().include_null_properties(include_null_properties=include_null_properties)
