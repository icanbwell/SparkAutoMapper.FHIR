from typing import Optional, Any

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.base64Binary import FhirBase64Binary
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class Extension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: FhirUri,
        valueCoding: Optional[Coding[Any]] = None,
        valueCode: Optional[FhirValueSetBase] = None,
        valueString: Optional[FhirString] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueInteger: Optional[FhirPositiveInt] = None,
        valuePositiveInt: Optional[FhirPositiveInt] = None,
        valueDecimal: Optional[FhirDecimal] = None,
        valueUri: Optional[FhirUri] = None,
        valueUrl: Optional[FhirUri] = None,
        valueBase64Binary: Optional[FhirBase64Binary] = None,
        valueDate: Optional[FhirDate] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valueReference: Optional[FhirResourceBase] = None,
        extension: Optional[FhirList['Extension']] = None
    ) -> None:
        """
        Extension type in FHIR
        https://www.hl7.org/fhir/extensibility.html
        Optional Extensions Element
        + Rule: Must have either extensions or value[x], not both


        :param url: identifies the meaning of the extension
        :param valueCoding: Value of extension
        :param valueCode: Value of extension
        :param valueString: Value of extension
        :param valueBoolean: Value of extension
        :param valueInteger: Value of extension
        :param valuePositiveInt: Value of extension
        :param valueDecimal: Value of extension
        :param valueUri: Value of extension
        :param valueUrl: Value of extension
        :param valueBase64Binary: Value of extension
        :param valueDate: Value of extension
        :param valueDateTime: Value of extension
        :param valueReference: Value of extension
        :param extension: list of sub extensions
        """
        super().__init__(
            url=url,
            valueCoding=valueCoding,
            valueCode=valueCode,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valuePositiveInt=valuePositiveInt,
            valueDecimal=valueDecimal,
            valueUri=valueUri,
            valueUrl=valueUrl,
            valueBase64Binary=valueBase64Binary,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueReference=valueReference,
            extension=extension
        )
