from typing import Optional, Any

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.identifier import Identifier

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.complex_types.money import Money

from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.fhir_types.id import FhirId

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
        id_: Optional[FhirId],
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
        extension: Optional[FhirList['Extension']] = None,
        valueId: Optional[FhirId] = None,
        valueTime: Optional[FhirDateTime] = None,
        valueUnsignedInt: Optional[FhirPositiveInt] = None,
        valueCodeableConcept: Optional[CodeableConcept[FhirValueSetBase]
                                       ] = None,
        valueCount: Optional[FhirPositiveInt] = None,
        valueMoney: Optional[Money] = None,
        valuePeriod: Optional[Period] = None,
        valueQuantity: Optional[Quantity] = None,
        valueIdentifier: Optional[Identifier] = None,
        valueRange: Optional[Range] = None
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
            id_=id_,
            extension=extension,
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
            valueBase64Binary=valueBase64Binary,
            valueCodeableConcept=valueCodeableConcept,
            valueCoding=valueCoding,
            valueCount=valueCount,
            valueIdentifier=valueIdentifier,
            valueMoney=valueMoney,
            valuePeriod=valuePeriod,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueReference=valueReference
        )
